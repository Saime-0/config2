#!/bin/bash

set -e
login=okg0
useradd -m -G wheel $login
echo "%wheel  ALL=(ALL:ALL)    NOPASSWD:SETENV: ALL" > /etc/sudoers.d/wheel
passwd $login