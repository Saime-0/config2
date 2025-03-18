#!/bin/bash

set -e
login=okg0
useradd -m -G wheel $login
passwd $login