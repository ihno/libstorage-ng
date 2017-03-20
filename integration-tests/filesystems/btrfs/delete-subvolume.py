#!/usr/bin/python

# requirements: btrfs on /dev/system/btrfs with test subvolume


from storage import *
from storageitu import *


set_logger(get_logfile_logger())

environment = Environment(False)

storage = Storage(environment)

staging = storage.get_staging()

print staging

blk_device = BlkDevice.find_by_name(staging, "/dev/system/btrfs")
btrfs = to_btrfs(blk_device.get_blk_filesystem())

btrfs_subvolume = btrfs.find_btrfs_subvolume_by_path("test")

staging.remove_device(btrfs_subvolume)

print staging

commit(storage, skip_save_graphs = False)

