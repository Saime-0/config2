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

#fonts
paru.install(fonts_pkg_names)

# de
paru.install(xfce.pkg_names)
xfce.setup()

# Install opt packages
opt_pkgs = [
    vscode,
    terminus_font,
    alacritty,
]
opt_pkgs_names = [
    "ly",

    "go",
    "delve",
    "go-mockery",
    "gopls",
    "jdk-openjdk",

    "qbittorrent",
    "golangci-lint",
    "obs-studio",
    "libreoffice-still",
] + [p.pkg_name for p in opt_pkgs]
paru.install(opt_pkgs_names)

# Setup opt packages
for p in opt_pkgs:
    if hasattr(p, 'setup') and callable(getattr(p, 'setup')):
        p.setup()
