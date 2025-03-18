import os
import subprocess

class pacman:
    pkg_name = "pacman"
    bin = "pacman"
        
    def install(packages: list[str], no_confirm: bool = False, needed: bool = False, sysroot: os.path = "/") -> bool:
        cmd = ["sudo", pacman.bin, "-Sy", ' '.join(packages)]
        if no_confirm: cmd.append("--noconfirm")
        if needed: cmd.append("--needed")
        if sysroot: cmd.append(f"--sysroot={sysroot}")
        print(cmd)
        subprocess.run(cmd, shell=True, check=True, text=True)

    def setup():
        print("pacman:setup:TODO")

from pkgs.list import list as pkgs_list; pkgs_list.append(pacman)