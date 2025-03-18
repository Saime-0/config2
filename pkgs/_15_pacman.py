import os
import subprocess
from lib.package import Package

class pacman:
    def id()->str:
        return "pacman"
    
    def bin()->str:
        return "pacman"
        
    def install(packages: list[Package], no_confirm: bool = False, needed: bool = False, sysroot: os.path = "/") -> bool:
        cmd = [pacman.bin(), "-Sy"]
        if no_confirm: cmd.append("--noconfirm")
        if needed: cmd.append("--needed")
        if sysroot: cmd.append(f"--sysroot={sysroot}")
        subprocess.run(cmd)

    def setup():
        print("pacman:setup:TODO")

from pkgs.list import list as pkgs_list; pkgs_list.append(pacman)