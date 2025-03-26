#!/bin/bash

set -e

echo "Checking if the device exists ..."
if [ ! -e "$DEVICE" ]; then
  echo "Error: Device '$DEVICE' (\$DEVICE) not found."
  exit 1
fi

# echo "Clearing the partition table ..."
# sfdisk --delete $DEVICE

echo "Create partitions ..."
parted --script ${DEVICE} -- mklabel gpt
parted --script ${DEVICE} -- mkpart esp fat32 1MiB 512MiB
parted --script ${DEVICE} -- mkpart primary 512MiB 100%
parted --script ${DEVICE} -- set 1 boot on

# Даем время системе обновить информацию о разделах
sleep 2

echo "The disk partition is complete."
