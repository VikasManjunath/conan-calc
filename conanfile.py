from conans import ConanFile, CMake
import re, os

class CalculatorConan(ConanFile):
    name = "calculator"
    version = ""
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Calculator here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "src/*"
    exports="versions.txt"
    reference = name +"/" 
    versions = {}

    def __init__(self, output, runner, display_name="", user=None, channel=None):
        self.load_versions()
        super().__init__(output, runner, display_name=display_name, user=user, channel=channel)

    def load_versions(self):
        if(not self.versions): #if empty
            version_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "versions.txt"), 'r')
            for line in version_file.readlines():
                if line.isspace() or line[0]=='#':
                    continue
                kv = line.split("=")
                self.versions[kv[0].strip()]=kv[1].strip()

    def set_version(self):    
        self.version = str(self.versions.get("SELF_VERSION"))
        self.reference=self.reference+self.version


    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["calculator"]
