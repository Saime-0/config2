#!/bin/bash

set -e

scripts_dir="/mnt/root/tmp/install$(date +%s)"
mkdir $scripts_dir
parent_dir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")
cp $parent_dir/065_chroot/* $scripts_dir
arch-chroot /mnt bash -c "${scripts_dir}/*"
