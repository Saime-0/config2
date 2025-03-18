import os
from lib.package import Package

class nix:
    def id()->str:
        return "nix"
    
    def bin()->str:
        return "nix"
        
    def install(packages: list[Package], no_confirm: bool = False, needed: bool = False, sysroot: os.path = "/") -> bool:
        print(f"{id} -> install: pkgs:")
        for p in packages:
            print(p.id())
        print(f"{id} -> install: ok")
        
from pkgs.list import list as pkgs_list; pkgs_list.append(nix)