import os

class nix:
    pkg_name = "nix"
    bin = "nix"
        
    def install(
                packages: list[str],
                no_confirm: bool = True, 
                needed: bool = True,
                sysroot: str = "/",
                ) -> bool:
        print(f"{id} -> install: pkgs:")
        for p in packages:
            print(p.id())
        print(f"{id} -> install: ok")