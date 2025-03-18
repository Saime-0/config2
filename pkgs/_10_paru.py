import os
import subprocess
import time

class paru:
    pkg_name = "paru"

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

    
    def bin()->str:
        return "paru"
        
    def install(
                packages: list[str],
                no_confirm: bool = True, 
                needed: bool = True,
                sysroot: str = None,
                ) -> bool:
        subprocess.run([
            paru.bin,
            "-Sy",
            *packages,
            "--noconfirm" if no_confirm else "",
            "--needed" if needed else "",
            f"--sysroot={sysroot}" if sysroot else "",
        ], shell=True, check=True, text=True)

    def setup():
        print("paru:setup:TODO")