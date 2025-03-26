import os
import subprocess
import shutil

script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../dotfiles/.config/pacman.conf")
config_dst = os.path.expanduser("~/.config/pacman.conf")

class pacman:
    pkg_name = "pacman"
    bin = "pacman"
        
    def install(
                packages: list[str],
                no_confirm: bool = True, 
                needed: bool = True,
                sysroot: str = None,
                ) -> bool:
        subprocess.run(' '.join([
            "sudo",
            pacman.bin,
            "-Sy",
            *packages,
            "--noconfirm" if no_confirm else "",
            "--needed" if needed else "",
            f"--sysroot={sysroot}" if sysroot else "",
        ]), shell=True, check=True, text=True)

    def setup():
        # Скопировать конфиг
        shutil.copy2(config_src, config_dst)