import os
import subprocess
import shutil
import time

script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../dotfiles/.config/paru")
config_dst = os.path.expanduser("~/.config/paru")

class paru:
    pkg_name = "paru"
    bin = "paru"

    def get():
        dir=f"/tmp/paru{int(time.time())}"
        subprocess.run(f"git clone https://aur.archlinux.org/paru.git {dir}", shell=True, check=True, text=True)
        subprocess.run(f"makepkg -si -D {dir}", shell=True, check=True, text=True) 
        
    def install(
                packages: list[str],
                no_confirm: bool = True, 
                needed: bool = True,
                sysroot: str = None,
                ) -> bool:
        subprocess.run(' '.join([
            paru.bin,
            "-Sy",
            *packages,
            "--noconfirm" if no_confirm else "",
            "--needed" if needed else "",
            f"--sysroot={sysroot}" if sysroot else "",
        ]), shell=True, check=True, text=True)

    def setup():
        # Скопировать конфиг
        shutil.copytree(config_src, config_dst)