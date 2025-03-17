import argparse
import os
import importlib.util
from typing import Dict, Type, Optional

class PackageManager:
    """Интерфейс для пакетных менеджеров."""
    def install(self, package_name: str) -> bool:
        raise NotImplementedError


# Название файла с реализацией интерфейса
PM_FILENAME = "package_manager.py" 

def discover_package_managers(base_dir: str = "pkgs") -> Dict[str, Type[PackageManager]]:
    """
    Обнаруживает все реализации пакетных менеджеров в указанной директории.
    Возвращает словарь, где ключ — название директории, а значение — класс пакетного менеджера.
    """
    managers = {}
    for dir_name in os.listdir(base_dir):
        manager_dir = os.path.join(base_dir, dir_name)
        if os.path.isdir(manager_dir):
            module_path = os.path.join(manager_dir, PM_FILENAME)
            if os.path.exists(module_path):
                # Динамически загружаем модуль
                spec = importlib.util.spec_from_file_location("package_manager", module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Ищем класс, реализующий PackageManagerInterface
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if (
                        isinstance(attr, type)
                        and issubclass(attr, PackageManager)
                        and attr != PackageManager
                    ):
                        managers[dir_name] = attr
                        break
    return managers
def get_package_manager() -> PackageManager:
    """
    Возвращает экземпляр пакетного менеджера.
    Если передан аргумент --pm, использует указанный менеджер.
    Иначе выбирает первый доступный менеджер.
    """
    # Парсим аргумент --pm
    parser = argparse.ArgumentParser()
    parser.add_argument("--pm", type=str, help="Предпочтительный пакетный менеджер (например, yay).")
    args, _ = parser.parse_known_args()  # Игнорируем остальные аргументы

    # Обнаруживаем доступные менеджеры
    managers = discover_package_managers()

    # Если указан предпочтительный менеджер, используем его
    if args.pm and args.pm in managers:
        return managers[args.pm]()

    # Иначе выбираем первый доступный менеджер
    for manager_name, manager_class in managers.items():
        if manager_class.is_available():
            return manager_class()