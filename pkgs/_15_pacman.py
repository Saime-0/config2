import os
import subprocess

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
        print("pacman:setup:TODO")