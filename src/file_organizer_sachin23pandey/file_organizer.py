


import os
import shutil

def organize_file(path):
    files = os.listdir(path)

    for i in files:
        filename, extension = os.path.splitext(i)
        extension_1 = extension[1:] 
        if not extension_1: 
            continue

        folder_path = os.path.join(path, extension_1)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(os.path.join(path, i), os.path.join(folder_path, i))


def create_file(path, filename):
    file_path = os.path.join(path, filename)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass  # Create an empty file
        print(f"File created: {file_path}")
    else:
        print(f"File already exists: {file_path}")


def create_folder(path, foldername):
    folder_path = os.path.join(path, foldername)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")


def delete_file(path, filename):
    file_path = os.path.join(path, filename)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        os.remove(file_path)
        print(f"File deleted: {file_path}")
    else:
        print(f"File not found: {file_path}")


def delete_folder(path, foldername):
    folder_path = os.path.join(path, foldername)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"Folder deleted: {folder_path}")
    else:
        print(f"Folder not found: {folder_path}")


def rename_file(path, old_name, new_name):
    old_path = os.path.join(path, old_name)
    new_path = os.path.join(path, new_name)
    if os.path.exists(old_path) and os.path.isfile(old_path):
        os.rename(old_path, new_path)
        print(f"File renamed from {old_path} to {new_path}")
    else:
        print(f"File not found: {old_path}")


def rename_folder(path, old_name, new_name):
    old_path = os.path.join(path, old_name)
    new_path = os.path.join(path, new_name)
    if os.path.exists(old_path) and os.path.isdir(old_path):
        os.rename(old_path, new_path)
        print(f"Folder renamed from {old_path} to {new_path}")
    else:
        print(f"Folder not found: {old_path}")

