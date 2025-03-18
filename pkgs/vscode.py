import subprocess
import os
import shutil

extensions = [
    "alefragnani.bookmarks",
    "elszon.golang-regroup-imports",
    "emmanuelbeziat.vscode-great-icons",
    "golang.go",
    "gruntfuggly.todo-tree",
    "ionutvmi.path-autocomplete",
    "jnoortheen.nix-ide",
    "metaphore.kanagawa-vscode-color-theme",
    "ms-python.debugpy",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "r3inbowari.gomodexplorer",
    "streetsidesoftware.code-spell-checker",
    "yzhang.markdown-all-in-one",
]

script_dir = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_dir, "../dotfiles/.config/Code/User/settings.json")
config_dir=os.path.expanduser("~/.config/Code/User")
config_file=os.path.join(config_dir,"settings.json")
# from  lib.package import Package
class vscode():
    def id() -> str:
        return "vscode"

    def setup():
        # Скопировать конфиг
        os.makedirs(config_dir, exist_ok=True)
        shutil.copy2(config_src, config_file)

        # Установка расширений
        for ext in extensions:
            subprocess.run(["code", "--install-extension", ext])
