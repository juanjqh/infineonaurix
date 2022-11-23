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

from os.path import isdir, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()
board_config = env.BoardConfig()

FRAMEWORK_DIR = platform.get_package_dir("framework-aurduino")
assert isdir(FRAMEWORK_DIR)

BOARD = board_config.get("build.hardware")
MCU = board_config.get("build.variant")

TC275_INC = [

    join(FRAMEWORK_DIR, BOARD, "aurix/cores/aurduino"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Scu/Std"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Stm/Std"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Cpu/Irq"),
    join(FRAMEWORK_DIR, BOARD,"aurix/variants", MCU, "iLLD/Include/_Lib/DataHandling"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Cpu/Std"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU),
    join(FRAMEWORK_DIR, BOARD, "aurix/cores/aurduino/avr"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/_Build"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include"),
    join(FRAMEWORK_DIR, BOARD, "aurix/system/libaurix/include"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/_Impl"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/_Lib"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/_PinMap"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/_Reg"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Asclin"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Ccu6"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Cif"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Cpu"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Dma"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Dsadc"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Dts"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Emem"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Eray"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Eth"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Fce"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Flash"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Gtm"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Hssl"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/I2c"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Iom"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Msc"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Mtu"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Multican"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Port"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Psi5"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Psi5s"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Qspi"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Scu"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Sent"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Src"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/SrvSw"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Stm"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "iLLD/Include/Vadc")

]

TC375_INC = [

    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Port/Std"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/system/libaurix/include/tC375"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Pms/Std"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Infra/Ssw/tC37AED/tricore"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Scu/Std"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Service/CpuGeneric"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Infra/Platform"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Infra/Sfr/tC37AED/_Reg"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Dma/Std"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/cores/aurduino"),  
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Scu"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Stm/Std"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Cpu/Irq"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/_Lib/DataHandling"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Cpu/Std"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/cores/aurduino/avr"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/_Build"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/system/libaurix/include"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/_Impl"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/_Lib"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/_PinMap"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Asclin"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Ccu6"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Cif"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Cpu"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Dma"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Dts"), 
    join(FRAMEWORK_DIR, BOARD, "aurix/variants/tc375/iLLD/Include/Emem")

]

env.Append(
    ASFLAGS=["-Wa", "--gdwarf-2"],

    CFLAGS=[
        "-c",
        "-fno-common",
        # "-g3",   # Platmormio adds -g2 flag when compiled in debugger mode#
        # "-MMD",  # necessary?
        # "-MP",   # necessary?
        # "-MF",   # necessary?
        "-W",
        "-Wextra",
        "-Wdiv-by-zero",
        "-Warray-bounds",
        "-Wcast-align",
        "-Wignored-qualifiers",
        "-Wformat",
        "-Wformat-security",
        "-fshort-double",
        "-include",
        "Variant.h",
        "-mversion-info"

    ],

    CXXFLAGS=[
        "-std=c++14",
        "-fno-common",
        # "-g3",  # Platmormio adds -g2 flag when compiled in debugger mode#
        # "-MMD", # necessary?
        # "-MP",  # necessary?
        # "-MF",  # necessary?
        "-W",
        "-Wextra",
        "-Wdiv-by-zero",
        "-Warray-bounds",
        "-Wcast-align",
        "-Wignored-qualifiers",
        "-Wformat",
        "-Wformat-security",
        "-fshort-double",
        "-include",
        "Variant.h",
        "-mversion-info"
    ],

    LINKFLAGS=[
        "-nocrt0",
        "-Wl,--gc-sections",
        '"-Wl,-Map=' + join("$BUILD_DIR", "${PROGNAME}.map") + '"',
        "-Wl,--cref",
        "-Wl,--gc-sections",
        "-fshort-double",
        "-Wl,--mem-holes"
    ],

    LIBPATH=[
        join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU)
    ],

    LDSCRIPT_PATH=join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU, "linker_scripts/gcc/iROM.ld")
)

if board_config.get("build.mcu") == "tc37xx":
    env.Append(

        LINKFLAGS=["-mtc162"],

        CXXFLAGS=["-mtc162", "-Os"],

        CFLAGS=["-mtc162", "-Os"],

        LIBS=["Aurduino.a", "TriLib.a", "iLLD_Lib_Make_TC375.a"],

        CPPPATH=TC375_INC,

        CPPDEFINES=["TRIBOARD_TC37XA", "ARDUINO_ARCH_AURIX", "USE_IRQ", "__TC37XX__"],

    )
else:
    env.Append(

        LINKFLAGS="-mcpu=%s" % env.BoardConfig().get("build.mcu"),

        CXXFLAGS=["-mcpu=%s" % env.BoardConfig().get("build.mcu"), "-O2"],

        CFLAGS=["-mcpu=%s" % env.BoardConfig().get("build.mcu"), "-O2"],

        LIBS=["Aurduino.a", "TriLib.a", "iLLD_Lib_Make.a"],

        CPPPATH=TC275_INC,

        CPPDEFINES=["TRIBOARD_TC275C", "ARDUINO_ARCH_AURIX", "USE_IRQ"],

    )

env.Append(
    LIBSOURCE_DIRS=[
        join(FRAMEWORK_DIR, BOARD, "aurix/libraries")
    ]
)

#
# Target: Build 
#

libs = []

# env.BuildSources(
#     join("$BUILD_DIR", "aurix/cores"),
#     join(FRAMEWORK_DIR, BOARD, "aurix/cores")
# )
# env.BuildSources(
#     join("$BUILD_DIR", "aurix/variants"),
#     join(FRAMEWORK_DIR, BOARD, "aurix/variants")
# )
# env.BuildSources(
#     join("$BUILD_DIR", "aurix/system"),
#     join(FRAMEWORK_DIR, BOARD, "aurix/system")
# )

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "aurix"),
    join(FRAMEWORK_DIR, BOARD, "aurix"),
    src_filter="+<*> -<libraries> -<variants/" + MCU + "/crt0-tc*.c>"
))

env.BuildSources(
    join("$BUILD_DIR", "aurix"),
    join(FRAMEWORK_DIR, BOARD, "aurix/variants", MCU),
    src_filter="-<*> +<crt0-tc*.c>"
)

env.Prepend(LIBS=libs)
