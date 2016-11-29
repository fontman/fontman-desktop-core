""" Directories/files management

Basically help fms to create/remove/move files or directories.
Uses shutil high level python operations library and os python library.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 26/11/2016
"""

import os, os.path, requests, shutil


class FileManager:

    def create_directory(self, directory_path):
        try:
            if self.is_dir_exists(directory_path):
                print(directory_path + " already exists")
            else:
                os.makedirs(directory_path)
        except:
            raise

    def create_file(self, file_path):
        try:
            with open(file_path, "w") as stream:
                stream.write("[]")
        except:
            raise

    def copy_directory(self, source, destination):
        shutil.copytree(source, destination)

    def copy_file(self, file_name, source_dir, dest_dir):
        try:
            shutil.copyfile(
                source_dir + "/" + file_name,
                dest_dir + "/" + file_name
            )

        except:
            self.create_directory(dest_dir)
            self.copy_file(file_name, source_dir, dest_dir)
            
    def download_file(self, destination, url):
        with open(destination, "wb") as stream:
            stream.write(requests.get(url).content)

    def is_dir_exists(self, path):
        return os.path.isdir(path)

    def is_file_exists(self, path):
        return os.path.isfile(path)

    def move_directory(self, source, destination):
        shutil.move(source, destination)

    def move_file(self, file_name, source_dir, dest_dir):
        try:
            shutil.move(
                source_dir + "/" + file_name,
                dest_dir + "/" + file_name
            )

        except:
            self.create_directory(dest_dir)
            self.move_file(file_name, source_dir, dest_dir)
