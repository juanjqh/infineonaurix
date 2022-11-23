#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import makedirs
from os.path import isdir, join
from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment
from platform import system
import subprocess
env = DefaultEnvironment()

# A full list with the available variables
# http://www.scons.org/doc/production/HTML/scons-user.html#app-variables

if  env.BoardConfig().get("build.toolchain") == "hightec":

 env.Replace(

    AR="tricore-ar",
    AS="tricore-as",
    CC="tricore-gcc",
    CXX="tricore-g++",
    OBJCOPY="tricore-objcopy",
    SIZETOOL="tricore-size",
    OBJDUMP="tricore-objdump",
    RANLIB="tricore-ranlib",
    SIZEPRINTCMD='$SIZETOOL -d $SOURCES',
    PROGSUFFIX=".elf",

)

else:

 env.Replace(

    AR="tricore-elf-ar",
    AS="tricore-elf-as",
    CC="tricore-elf-gcc",
    CXX="tricore-elf-g++",
    OBJCOPY="tricore-elf-objcopy",
    SIZETOOL="tricore-elf-size",
    OBJDUMP="tricore-elf-objdump",
    RANLIB="tricore-elf-ranlib",
    SIZEPRINTCMD='$SIZETOOL -d $SOURCES',
    PROGSUFFIX=".elf",

)


if env.get("PROGNAME", "program") == "program":
    env.Replace(PROGNAME="firmware")

env.Append(

    BUILDERS=dict(
        ElfToLst=Builder(
            action=" ".join([
                "$OBJDUMP",
                "-S",
                "-d",
                "$SOURCES",
                ">$TARGET"]),
            suffix=".lst"
        ),
        ElfToHex=Builder(
            action=env.VerboseAction(" ".join([
                "$OBJCOPY",
                "-O",
                "ihex",
                "$SOURCES",
                "$TARGET"
            ]), "Building $TARGET"),
            suffix=".hex"
        )
    )
)

#
# Target: Build executable and linkable firmware
#

target_elf = None
if "nobuild" in COMMAND_LINE_TARGETS:
    target_elf = join("$BUILD_DIR", "${PROGNAME}.elf")
    target_firm = join("$BUILD_DIR", "${PROGNAME}.hex")
else:
    target_elf = env.BuildProgram()
    target_firm = env.ElfToHex(join("$BUILD_DIR", "${PROGNAME}"), target_elf)

AlwaysBuild(env.Alias("nobuild", target_firm))
target_buildprog = env.Alias("buildprog", target_firm, target_firm)


######################## Target reset post upload #####################
FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-aurduino")
MCU = env.BoardConfig().get("build.variant")

def after_upload(source, target, env):
    print("Resetting target...") 
    subprocess.call(join(FRAMEWORK_DIR, "utilities", MCU, "reset" + MCU + ".exe"))
#env.AddPostAction("upload", after_upload)

#
# Target: Upload firmware "Using Infineon IMTmemtool"
#

def _imtmemtool_cmd_script(env, source):
    build_dir = env.subst("$BUILD_DIR")
    firmwarePath = join(build_dir, "firmware.hex")
    if not isdir(build_dir):
        makedirs(build_dir)
    script_path = join(build_dir, "upload.mtb")
    commands = [
        "open_file %s" % firmwarePath,
        "connect",
        "select_all_sections",
        "add_selected_sections",
        "program",
        "disconnect",
        "exit"
    ]
    with open(script_path, "w") as fp:
        fp.write("\n".join(commands))
    return script_path

imtMemtool_Cfg = env.BoardConfig().get("upload.das_cfg")

if env.BoardConfig().get("upload.tool") == "infineonmemtool":
    env.Replace(
    __imtmemtool_cmd_script=_imtmemtool_cmd_script,
    UPLOADER="IMTMemtool.exe" if system() == "Windows" else "IMTMemtool",
    UPLOADERFLAGS=["-c", 
    join(FRAMEWORK_DIR, "utilities", MCU, imtMemtool_Cfg)
    ],
    UPLOADCMD='$UPLOADER $UPLOADERFLAGS "${__imtmemtool_cmd_script(__env__, SOURCE)}"'
    )
    env.AddPostAction("upload", after_upload)
    
#
# Target: Upload firmware "Using AurixFlasher tool from Infineon Aurix Development Studio"
# 

else: # AurixFlaher tool is the DEFAULT option in board configuration
    env.Replace(
    UPLOADER="AurixFlasher.exe" if system() == "Windows" else "AurixFlasher",
    UPLOADERFLAGS=["-hex", join(env.subst("$BUILD_DIR"), "firmware.hex")],
    UPLOADCMD='$UPLOADER $UPLOADERFLAGS'
    )
    

upload_actions = [env.VerboseAction("$UPLOADCMD", "Uploading $SOURCE")]
AlwaysBuild(env.Alias("upload", target_firm, upload_actions))
    

#
# Target: Print binary size
#

target_size = env.Alias(
    "size", target_elf,
    env.VerboseAction("$SIZEPRINTCMD", "Calculating size $SOURCE"))

AlwaysBuild(target_size)

#
# Target: Define targets
#

Default([target_buildprog, target_size])
