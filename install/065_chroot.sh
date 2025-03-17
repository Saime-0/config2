#!/bin/bash

set -e

scripts_dir="/tmp/install$(date +%s)"
mkdir /mnt$scripts_dir
parent_dir=$(dirname -- "$(readlink -f -- "$BASH_SOURCE")")
cp $parent_dir/065_chroot/* /mnt$scripts_dir

for script in $(ls /mnt$scripts_dir); do
    echo "Running the script: $script"
    arch-chroot /mnt /bash -c $script
    # bash $scripts_dir/$script
    # Проверка кода завершения
    if [ $? -ne 0 ]; then
        echo "Error: the $script script failed with an error. Execution stopped."
        exit 1
    fi
done
