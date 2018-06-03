#!/bin/bash
# oceanos-download.sh
#
# Install on Remote PCs
#
# rsync tool to download server data
# from remote.server.com
# to local computer
#
# uses ssh key pairs to login automatically
#
# last edited: 15/01/2017 by tgeo
#
# download only those files on remote.server.com in Downloads and Downloads40G directories
# that are newer than what is already on local computer. keep track of what is already downloaded
# in prev-downloads.log

set -x #echo on

# Downloads folder

rsync -avzu --exclude-from=prev-downloads.log -h --progress root@remote.server.com:/home/user/Downloads/ /cygdrive/g/#oceanos-SYNC/Downloads/ | tee -a prev-downloads.log

# Downloads40G folder

rsync -avzu --exclude-from=prev-downloads.log -h --progress root@remote.server.com:/home/user/Downloads40G/ /cygdrive/g/#oceanos-SYNC/Downloads40G/ | tee -a prev-downloads.log
