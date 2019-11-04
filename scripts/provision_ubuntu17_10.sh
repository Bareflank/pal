#!/bin/bash -e

sudo apt-get update
sudo apt-get install -y git python3 python3-pip gcc-aarch64-linux-gnu \
    g++-aarch64-linux-gnu qemu-system-arm qemu-efi

sudo pip3 install lxml colorama coverage
