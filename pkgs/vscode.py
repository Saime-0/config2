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

script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../dotfiles/.config/Code")
config_dst = os.path.expanduser("~/.config/Code")

class vscode():
    pkg_name = "vscode"

    def setup():
        # Скопировать конфиг
        shutil.copytree(config_src, config_dst, dirs_exist_ok=True)

        # Установка расширений
        for ext in extensions:
            subprocess.run(["code", "--install-extension", ext])
