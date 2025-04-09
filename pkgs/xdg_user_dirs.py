import os
import shutil
import subprocess
import os

script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../dotfiles/.config/user-dirs.dirs")
config_dst = os.path.expanduser("~/.config/user-dirs.dirs")

class xdg_user_dirs:
    pkg_name = "xdg-user-dirs"

    def setup():
        # Скопировать конфиг
        shutil.copy2(config_src, config_dst)
        # Сгеренировать директории
        subprocess.run('mkdir downloads', shell=True, check=True, text=True)
        subprocess.run('ln -s downloads Downloads', shell=True, check=True, text=True)
        subprocess.run('xdg-user-dirs-update', shell=True, check=True, text=True)
        

        
