import subprocess
import os
import shutil


script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../dotfiles/etc/vconsole.conf")
config_dst = "/etc/vconsole.conf"

class terminus_font:
    pkg_name = "terminus-font"
    
    def setup():
        with open(config_src, 'r') as file:
            content = file.read()

        subprocess.run(f'sudo tee {config_dst}', input=content.encode(), check=True)