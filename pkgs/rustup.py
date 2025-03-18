import subprocess
import os
import shutil

class rustup():
    pkg_name = "rustup"

    def setup():
        subprocess.run('rustup default stable', shell=True, check=True, text=True)
