# common code and can be copied to any optimus project
from cpt.packager import ConanMultiPackager
import platform
from conans.tools import load
import re, os


class PackageUtil:
    versions={}
    
    def __init__(self) -> None:
        self.load_versions()

    def setup_linux(self,settings:dict):
        settings['compiler'] = "gcc"
        settings['compiler.libcxx'] = "libstdc++11"
                    
    def setup_mac(self,settings:dict):
        settings['compiler'] = "apple-clang"
        settings['compiler.cppstd'] = "20"

    def load_versions(self):
            version_file = open(os.path.join(os.getcwd(), "versions.txt"), 'r')
            for line in version_file.readlines():
                if line.isspace() or line[0]=='#':
                    continue
                kv = line.split("=")
                self.versions[kv[0].strip()]=kv[1].strip()    


    def setup(self,builder:ConanMultiPackager):          
        release_settings={"arch": "x86_64", "build_type": "Release"}
        os=platform.system()
        if os =="Darwin":
            self.setup_mac(release_settings)
        elif os=="Linux":
            self.setup_linux(release_settings)
        else: 
            print("Not supported OS")

        debug_settings = release_settings.copy()
        debug_settings['build_type']="Debug"
        builder.add(release_settings,options={}, env_vars={}, build_requires={})       
        builder.add(debug_settings,options={}, env_vars={}, build_requires={})

    # end of PackageUtil class   

if __name__ == "__main__":
    package_util = PackageUtil()
    ver_ref = "calculator/" + str(package_util.versions.get("SELF_VERSION"))
    builder = ConanMultiPackager(username="master",reference=ver_ref)      
    builder.build_policy="missing"
    package_util.setup(builder)
    builder.run()