import os
from lib.package import Package
import subprocess
import time

class paru:
    def get():
        def run_command(command):
            return subprocess.run(command, shell=True, check=True, text=True)
        try:
            dir=f"/tmp/paru{int(time.time())}"
            run_command(f"git clone https://aur.archlinux.org/paru.git {dir}")
            run_command(f"makepkg -si -D {dir}")
            print("Скрипт выполнен успешно.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении команды: {e}")    

    def id()->str:
        return "paru"
    
    def bin()->str:
        return "paru"
        
    def install(packages: list[Package], no_confirm: bool = False, needed: bool = False, sysroot: str = "/") -> bool:
        cmd = [paru.bin(), "-Sy"]
        if no_confirm: cmd.append("--noconfirm")
        if needed: cmd.append("--needed")
        if sysroot: cmd.append(f"--sysroot={sysroot}")
        subprocess.run(cmd)

    def setup():
        print("paru:setup:TODO")

from pkgs.list import list as pkgs_list; pkgs_list.append(paru)