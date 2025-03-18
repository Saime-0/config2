import os
import importlib.util
from lib.package  import Package
from lib.package_manager  import PackageManager
import importlib
import inspect
from shutil import which
from typing import Type


def get_package_manager() -> Type[PackageManager]:
    # Путь к директории с классами
    base_dir = os.path.abspath("pkgs")
    # Импортируем все модули из директории pkgs
    for scriptname in os.listdir(base_dir):
        if not os.path.isfile(os.path.join(base_dir, scriptname)):
            continue

        filename = scriptname.removesuffix(".py")
        if filename == scriptname:
            continue

        module = importlib.import_module(f"pkgs.{filename}")

        # Ищем все классы в модуле
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # Проверяем, реализует ли класс интерфейс PackageManager
            # if obj == PackageManager:
            #     continue

            
            # id = getattr(obj, "id", None)
            # install = getattr(obj, "install", None)
            if hasattr(obj, "id"):
                # Проверяем, существует ли программа в системе по id
                instance = obj()
                print (instance.id())
                if which(instance.id()):
                    return instance

    raise RuntimeError("Ни один подходящий менеджер пакетов не найден в системе.")

# Пример использования
if __name__ == "__main__":
    try:
        PackageManagerClass = get_package_manager()
        print(f"Найден менеджер пакетов: {PackageManagerClass.__name__}")
    except RuntimeError as e:
        print(e)