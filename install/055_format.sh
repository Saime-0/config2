#!/bin/bash

set -e

echo "Checking if the device exists ..."
if [ ! -e "$DEVICE" ]; then
  echo "Error: Device '$DEVICE' (\$DEVICE) not found."
  exit 1
fi

# Определяем суффикс раздела
DEVICE_NAME=$(basename "$DEVICE")
if [[ "$DEVICE_NAME" == nvme* ]]; then
    PART_SUFFIX="p"
else
    PART_SUFFIX=""
fi

echo "Formatting partitions ..."
mkfs.fat -F 32 "${DEVICE}${PART_SUFFIX}1"  # EFI раздел
fatlabel "${DEVICE}${PART_SUFFIX}1" BOOT
mkfs.ext4 "${DEVICE}${PART_SUFFIX}2" -L ROOT      # Root раздел
