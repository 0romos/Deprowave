#!/usr/bin/env python3

import os
import sys
import stat
import datetime

def print_folders_and_files(root_path, show_hidden=False):
    items = os.listdir(root_path)

    hidden_folders = []
    hidden_files = []
    folders = []
    files = []

    for item in items:
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            if item.startswith('.') and show_hidden:
                hidden_folders.append(item)
            elif not item.startswith('.'):
                folders.append(item)
        else:
            if item.startswith('.') and show_hidden:
                hidden_files.append(item)
            elif not item.startswith('.'):
                files.append(item)

    hidden_folders.sort()
    hidden_files.sort()
    folders.sort()
    files.sort()

    for folder in hidden_folders + folders:
        folder_path = os.path.join(root_path, folder)
        folder_stat = os.stat(folder_path)
        mode = folder_stat.st_mode
        mode_str = format(stat.filemode(mode), '10s')
        nlink = folder_stat.st_nlink
        uid = folder_stat.st_uid
        gid = folder_stat.st_gid
        size = folder_stat.st_size
        mtime = folder_stat.st_mtime
        mtime_str = datetime.datetime.fromtimestamp(mtime).strftime('%b %d %H:%M')
        print(f"{mode_str} {nlink:<4d} {uid:<4d} {gid:<4d} {size:<8d} {mtime_str}   {folder}")

    for file in hidden_files + files:
        file_path = os.path.join(root_path, file)
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode
        mode_str = format(stat.filemode(mode), '10s')
        nlink = file_stat.st_nlink
        uid = file_stat.st_uid
        gid = file_stat.st_gid
        size = file_stat.st_size
        mtime = file_stat.st_mtime
        mtime_str = datetime.datetime.fromtimestamp(mtime).strftime('%b %d %H:%M')
        print(f"{mode_str} {nlink:<4d} {uid:<4d} {gid:<4d} {size:<8d} {mtime_str}   {file}")

if len(sys.argv) > 1:
    directory_path = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == '-a':
        show_hidden = True
    else:
        show_hidden = False
else:
    directory_path = os.getcwd()
    show_hidden = False

print_folders_and_files(directory_path, show_hidden)
