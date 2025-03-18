import os

class PackageManager:
    @property
    def bin() -> str:
        raise NotImplementedError
    
    def install(self, packages: list[str], no_confirm: bool = False, needed: bool = False, sysroot: os.path = os.path.abspath("/")) -> bool:
        raise NotImplementedError
