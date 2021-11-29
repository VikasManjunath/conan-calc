from cpt.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager(username="vikas")
    builder.build_policy="missing"
    
    builder.add(settings={"arch": "x86_64", "build_type": "Debug","compiler.cppstd":"20"},
                options={}, env_vars={}, build_requires={})
    builder.add(settings={"arch": "x86_64", "build_type": "Release","compiler.cppstd":"20"},
                options={}, env_vars={}, build_requires={})

    if platform.system=="Darwin":
        builder.compiler.libcxx="libstdc++11"
    builder.run()