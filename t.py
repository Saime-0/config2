import os
import importlib.util
from lib import Package
from lib import PackageManager
import importlib
import inspect
from shutil import which
from typing import Type
import inspect
import pkgutil
import pkgs

def is_pkg_mgr(cls) -> bool:
    return hasattr(cls, 'install') and hasattr(cls, 'bin')

# def is_pkg_mgr2(cls) -> bool:
#     base_attrs = {name: getattr(PackageManager, name) for name in dir(PackageManager) if not name.startswith('__')}

#     for name, attr in base_attrs.items():
#         if not hasattr(cls, name):
#             return False
#         # Проверяем, что атрибуты являются вызываемыми (если это метод) или свойствами
#         if inspect.isfunction(attr):
#             if not callable(getattr(cls, name)):
#                 return False
#         elif isinstance(attr, property):
#             if not isinstance(getattr(cls, name), property):
#                 return False
#         return False

def getpm2(module) -> Type[PackageManager]:
    for _, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and is_pkg_mgr(obj) and which(obj.bin()):
            return obj
    
    for name, pkg in inspect.getmembers(module):
        print(name)
        if name.startswith("__") or not inspect.ismodule(pkg):
            continue
        for _, obj in inspect.getmembers(pkg):
            if inspect.isclass(obj) and is_pkg_mgr(obj) and which(obj.bin()):
                return obj
            
    print("[ERROR] Ни один подходящий менеджер пакетов не найден в системе.")
    return None

        # Если это подмодуль, рекурсивно собираем классы из него
        # elif inspect.ismodule(obj):
        #     classes_list.extend(getpm2(obj))



# Путь к директории с файлами
# directory = 'package_managers'

# def getpm()-> Type[PackageManager]:
#     # Список для хранения классов
#     # classes_list: list[Type[PackageManager]]= []

#     # Проходим по всем файлам в директории
#     for filename in os.listdir(directory):
#         if filename.endswith('.py') and filename != '__init__.py':
#             # Получаем имя класса (без .py)
#             class_name = filename.removesuffix(".py")
#             # print(class_name)
#             # Импортируем модуль
#             module = importlib.import_module(f'{directory}.{class_name}')
            
#             # Получаем класс из модуля
#             cls:Type[PackageManager]  = getattr(module, class_name)
#             if which(cls.bin()):
#                 return cls
            
#     raise RuntimeError("Ни один подходящий менеджер пакетов не найден в системе.")


# def get_package_manager() -> Type[PackageManager]:
#     # Путь к директории с классами
#     base_dir = os.path.abspath("pkgs")
#     # Импортируем все модули из директории pkgs
#     for scriptname in os.listdir(base_dir):
#         if not os.path.isfile(os.path.join(base_dir, scriptname)):
#             continue

#         filename = scriptname.removesuffix(".py")
#         if filename == scriptname:
#             continue

#         module = importlib.import_module(f"pkgs.{filename}")

#         # Ищем все классы в модуле
#         for name, obj in inspect.getmembers(module, inspect.isclass):
#             # Проверяем, реализует ли класс интерфейс PackageManager
#             # if obj == PackageManager:
#             #     continue

            
#             print (name)
#             # id = getattr(obj, "id", None)
#             # install = getattr(obj, "install", None)
#             if hasattr(obj, "id"):
#                 # Проверяем, существует ли программа в системе по id
#                 instance = obj()
#                 if which(instance.id()):
#                     return instance

#     raise RuntimeError("Ни один подходящий менеджер пакетов не найден в системе.")
# from package_managers import * as

# from pkgs.list import list as pkgs_list

# def getpm3() -> Type[PackageManager]:
#     # print(pkgs_list)
#     for v in pkgs_list:
#         print(is_pkg_mgr(v))

# Пример использования
if __name__ == "__main__":
    try:
        # PackageManagerClass = get_package_manager()
        # print(f"Найден менеджер пакетов1: {getpm()}")
        print(f"Найден менеджер пакетов2: {getpm2(pkgs)}")
        # print(f"Найден менеджер пакетов3: {getpm3()}")
    except RuntimeError as e:
        print(e)