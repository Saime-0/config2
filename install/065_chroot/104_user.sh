#!/bin/bash

set -e
login=okg0
useradd -m -G $login
passwd $login