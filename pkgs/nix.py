import os
from lib.package import Package

class nix():
    def id(self)->str:
        "nix"
    
    def install(self, packages: list[Package], no_confirm: bool = False, needed: bool = False, sysroot: os.path = "/") -> bool:
        raise NotImplementedError