#!/bin/bash

set -e

scripts_dir="/mnt/tmp/install$(date +%s)"
mkdir $scripts_dir
cp ./065_chroot/* $scripts_dir
arch-chroot /mnt ${scripts_dir}/*
