#!/bin/bash

swapfile="/mnt/.swapfile"

dd if=/dev/zero of=${swapfile} bs=1024 count=2097152 # 2GB size
chmod 600 ${swapfile}
mkswap ${swapfile}
swapon ${swapfile}

echo "Создан swapfile."
