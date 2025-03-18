#!/bin/python

import pkgs
import lib

packages=[
    # pkgs.vscode
    pkgs.dummy
]

lib.get_package_manager(pkgs).install(packages)

for p in packages:
    if hasattr(p, 'setup') and callable(getattr(p, 'setup')):
        p.setup()
