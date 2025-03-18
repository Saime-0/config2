import os
from lib.package  import Package

class PackageManager:
    def id()->str:
        raise NotImplementedError
    def install(self, packages: list[Package], no_confirm: bool = False, needed: bool = False, sysroot: os.path = os.path.abspath("/")) -> bool:
        raise NotImplementedError
