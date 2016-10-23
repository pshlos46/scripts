#!/bin/sh

# Use it as a cron job to empty recycle bin periodically in file server. CentOS 7.

# Empty the trash.
rm -rf /home/user/.local/share/Trash/*

# Empty the trash of the virtual disk mount
rm -rf /mnt/vdb1/.Trash-1000/*
