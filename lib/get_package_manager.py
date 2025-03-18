from lib.package_manager  import PackageManager
import inspect
from shutil import which
from typing import Type
import inspect

def is_pkg_mgr(cls) -> bool:
    return hasattr(cls, 'install') and hasattr(cls, 'bin')

def get_package_manager(module) -> Type[PackageManager]:
    for name, obj in inspect.getmembers(module):
        if name.startswith("__"):
            continue
        if inspect.isclass(obj) and is_pkg_mgr(obj) and which(obj.bin):
            return obj
        
    raise RuntimeError("Ни один подходящий менеджер пакетов не найден в системе.")