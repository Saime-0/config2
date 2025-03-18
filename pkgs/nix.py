import os

class nix:
    pkg_name = "nix"
    bin = "nix"
        
    def install(packages: list[str], no_confirm: bool = False, needed: bool = False, sysroot: os.path = "/") -> bool:
        print(f"{id} -> install: pkgs:")
        for p in packages:
            print(p.id())
        print(f"{id} -> install: ok")
        
from pkgs.list import list as pkgs_list; pkgs_list.append(nix)