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
parted --script ${DEVICE} -- \
            mklabel gpt \ 
            mkpart esp fat32 1MiB 512MiB \
            mkpart primary 512MiB 100% \
            set 1 boot on

echo "The disk partition is complete."
