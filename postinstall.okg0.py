#!/bin/python

import pkgs
import lib

pkgs.paru.get()

packages = pkgs.base_packages + [
    pkgs.vscode,
    # pkgs.dummy
]

lib.get_package_manager(pkgs).install(packages)

for p in packages:
    if hasattr(p, 'setup') and callable(getattr(p, 'setup')):
        p.setup()
