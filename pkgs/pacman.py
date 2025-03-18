import os
from lib.package import Package

class pacman:
    def id()->str:
        return "pacman"
    
    def bin()->str:
        return "pacman"
        
    def install(packages: list[Package], no_confirm: bool = False, needed: bool = False, sysroot: os.path = "/") -> bool:
        print(f"{id} -> install: ok")

from pkgs.list import list as pkgs_list; pkgs_list.append(pacman)