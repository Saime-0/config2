#!/bin/python

import pkgs
import lib

pkgs.paru.get()
pkgs.paru.setup()

pkgs_for_install = pkgs.base_packages + [
    pkgs.vscode,
    # pkgs.dummy
]

lib.get_package_manager(pkgs).install(pkgs_for_install)

for p in pkgs_for_install:
    if hasattr(p, 'setup') and callable(getattr(p, 'setup')):
        p.setup()
