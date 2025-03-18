import subprocess
import os
import shutil

script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../dotfiles/.config/alacritty")
config_dst = os.path.expanduser("~/.config/alacritty")

class alacritty:
    pkg_name = "alacritty"

    def setup():
        # Скопировать конфиг
        shutil.copytree(config_src, config_dst, dirs_exist_ok=True)