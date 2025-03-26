import os
import shutil

script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../dotfiles/.bashrc")
config_dst = os.path.expanduser("~/.bashrc")

class bash:
    pkg_name = "bash"

    def setup():
        # Скопировать конфиг
        shutil.copy2(config_src, config_dst)
        