
from os.path import isdir, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()
board_config = env.BoardConfig()

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-aurix")
assert FRAMEWORK_DIR and isdir(FRAMEWORK_DIR)

env.Append(

    CPPPATH=[

        join(FRAMEWORK_DIR, "Configurations"),
        join(FRAMEWORK_DIR, "Libraries"),
        join(FRAMEWORK_DIR, "Libraries/Infra"),
        join(FRAMEWORK_DIR, "Libraries/Infra/Platform"),
        join(FRAMEWORK_DIR, "Libraries/Infra/Platform/Tricore"),
        join(FRAMEWORK_DIR, "Libraries/Infra/Platform/Tricore/Compilers"),
        join(FRAMEWORK_DIR, "Libraries/Infra/Sfr"),
        join(FRAMEWORK_DIR, "Libraries/Infra/Sfr/TC27D"),
        join(FRAMEWORK_DIR, "Libraries/Infra/Sfr/TC27D/_Reg"),
        join(FRAMEWORK_DIR, "Libraries/Service"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/If"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/If/Ccu6If"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/StdIf"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/SysSe"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/SysSe/Bsp"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/SysSe/Comm"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/SysSe/General"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/SysSe/Math"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/SysSe/Time"),
        join(FRAMEWORK_DIR, "Libraries/Service/CpuGeneric/_Utilities"),
        join(FRAMEWORK_DIR, "Libraries/iLLD"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Asclin"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Asclin/Asc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Asclin/Lin"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Asclin/Spi"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Asclin/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Ccu6"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Ccu6/Icu"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Ccu6/PwmBc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Ccu6/PwmHl"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Ccu6/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Ccu6/TPwm"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Ccu6/Timer"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Ccu6/TimerWithTrigger"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cif"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cif/Cam"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cif/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cpu"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cpu/CStart"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cpu/Irq"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cpu/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cpu/Trap"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dma"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dma/Dma"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dma/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dsadc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dsadc/Dsadc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dsadc/Rdc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dsadc/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dts"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dts/Dts"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Dts/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Emem"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Emem/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Eray"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Eray/Eray"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Eray/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Eth"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Eth/Phy_Pef7071"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Eth/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Fce"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Fce/Crc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Fce/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Flash"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Flash/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gpt12"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gpt12/IncrEnc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gpt12/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Atom"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Atom/Pwm"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Atom/PwmHl"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Atom/Timer"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Tim"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Tim/In"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Tom"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Tom/Pwm"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Tom/PwmHl"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Tom/Timer"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Gtm/Trig"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Hssl"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Hssl/Hssl"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Hssl/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/I2c"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/I2c/I2c"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/I2c/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Iom"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Iom/Driver"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Iom/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Msc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Msc/Msc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Msc/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Mtu"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Mtu/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Multican"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Multican/Can"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Multican/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Port"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Port/Io"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Port/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Psi5"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Psi5/Psi5"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Psi5/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Psi5s"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Psi5s/Psi5s"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Psi5s/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Qspi"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Qspi/SpiMaster"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Qspi/SpiSlave"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Qspi/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Scu"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Scu/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Sent"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Sent/Sent"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Sent/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Smu"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Smu/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Src"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Src/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Stm"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Stm/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Stm/Timer"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Vadc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Vadc/Adc"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Vadc/Std"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/_Impl"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/_Lib"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/_Lib/DataHandling"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/_Lib/InternalMux"),
        join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/_PinMap")
    ],

    ASFLAGS=[
        
        "-Wa",
        "--gdwarf-2",
        "-mtc161"
    ],

    CFLAGS=[

        "-std=c99",
        "-O0",
        "-g3",
        "-Wall",
        "-c",
        "-fmessage-length=0",
        "-fno-common",
        "-fstrict-volatile-bitfields",
        "-fdata-sections",
        "-ffunction-sections",
        "-Wmissing-include-dirs",
        "-mtc161"
    ],

    CXXFLAGS=[

        "-O2",
        "-g3",
        "-Wall",
        "-Wextra",
        "-Wmissing-declarations",
        "-Wmissing-include-dirs",
        "-std=c++14",
        "-c",
        "-fmessage-length=0",
        "-fno-common"
    ],


    LINKFLAGS=[

        "-nocrt0",
        "-Wl,--gc-sections",
        "-mtc161",
        '"-Wl,-Map=' + join("$BUILD_DIR", "${PROGNAME}.map") + '"',
    ],

    LDSCRIPT_PATH=join(FRAMEWORK_DIR, "ld/Lcf_Gnuc_Tricore_Tc.lsl")

)


#
# Target: Build sdk
#

libs = []

libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "Libraries"),
    join(FRAMEWORK_DIR, "Libraries"),
    #src_filter="+<*> -<../Libraries/iLLD/TC27D/Tricore/Cpu/Trap> -<../Libraries/iLLD/TC27D/Tricore/Cpu/CStart>",
    src_filter="+<*> -<iLLD/TC27D/Tricore/Cpu/Trap> -<iLLD/TC27D/Tricore/Cpu/CStart>",#!!
))

env.BuildSources(
    join("$BUILD_DIR", "Configurations"),
    join(FRAMEWORK_DIR, "Configurations")
)
env.BuildSources(
    join("$BUILD_DIR", "Tricore/CStart"),
    join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cpu/CStart")
)
env.BuildSources(
    join("$BUILD_DIR", "Tricore/Cpu"),
    join(FRAMEWORK_DIR, "Libraries/iLLD/TC27D/Tricore/Cpu/Trap")
)

env.Prepend(LIBS=libs)
