import os

class PackageManager:
    @property
    def bin() -> str:
        raise NotImplementedError
    
    def install(
                packages: list[str],
                no_confirm: bool = True, 
                needed: bool = True,
                sysroot: str = "/",
                ) -> bool:
        raise NotImplementedError
