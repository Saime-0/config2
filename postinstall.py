#!/bin/python

import pkgs

pkgs.pacman.setup()

# Install base packages
pkgs.pacman.install(pkgs.base_pkg_names)

# Get pacman wrapper
pkgs.paru.get()
pkgs.paru.setup()

# Install opt packages
opt_pkgs = [
    pkgs.vscode,
]
pkgs.paru.install([p.pkg_name for p in opt_pkgs])

# Setup opt packages
for p in opt_pkgs:
    if hasattr(p, 'setup') and callable(getattr(p, 'setup')):
        p.setup()
