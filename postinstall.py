#!/bin/python

from pkgs import *

pacman.setup()

# Install base packages
pacman.install(base_pkg_names)

# Get pacman wrapper
pacman.install([rustup.pkg_name])
rustup.setup()
paru.get()
paru.setup()

# Install opt packages
opt_pkgs = [
    vscode,
]
paru.install([p.pkg_name for p in opt_pkgs])

# Setup opt packages
for p in opt_pkgs:
    if hasattr(p, 'setup') and callable(getattr(p, 'setup')):
        p.setup()
