import os
import subprocess

class pacman:
    pkg_name = "pacman"
    bin = "pacman"
        
    def install(
                packages: list[str],
                no_confirm: bool = True, 
                needed: bool = True,
                sysroot: str = "/",
                ) -> bool:
        cmd = ["sudo", pacman.bin, "-Sy", ' '.join(packages)]
        if no_confirm: cmd.append("--noconfirm")
        if needed: cmd.append("--needed")
        if sysroot: cmd.append(f"--sysroot={sysroot}")
        print(cmd)
        subprocess.run(cmd, shell=True, check=True, text=True)

    def setup():
        print("pacman:setup:TODO")