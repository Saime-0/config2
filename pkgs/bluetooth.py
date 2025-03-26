import subprocess
import os
import shutil

script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../dotfiles/.config/xfce4")
config_dst=os.path.expanduser("~/.config/xfce4")

class bluetooth:
    pkg_names = [
        "bluez", # предоставляет стек протоколов Bluetooth
        "bluez-utils", # предоставляющий утилиту bluetoothctl
        "blueman", # Полнофункциональный менеджер Bluetooth
    ]
    pkg_name = ' '.join(pkg_names)
    
    def setup():
        subprocess.run('sudo systemctl enable --now bluetooth.service', shell=True, check=True, text=True)
        