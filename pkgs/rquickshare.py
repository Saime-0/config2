import os
import shutil

script_parent = os.path.dirname(os.path.abspath(__file__))
config_src = os.path.join(script_parent, "../.local/share/dev.mandre.rquickshare")
config_dst = os.path.expanduser("~/.local/share/dev.mandre.rquickshare")

class rquickshare:
    pkg_name = "r-quick-share"

    def setup():
        # Скопировать конфиг
        shutil.copytree(config_src, config_dst, dirs_exist_ok=True)