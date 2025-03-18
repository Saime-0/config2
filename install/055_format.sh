#!/bin/bash

set -e

echo "Checking if the device exists ..."
if [ ! -e "$DEVICE" ]; then
  echo "Error: Device '$DEVICE' (\$DEVICE) not found."
  exit 1
fi

echo "Formatting partitions ..."
mkfs.fat -F 32 ${DEVICE}1  # EFI раздел
fatlabel ${DEVICE}1 BOOT
mkfs.ext4 ${DEVICE}2 -L ROOT      # Root раздел
