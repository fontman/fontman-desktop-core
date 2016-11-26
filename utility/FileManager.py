""" Directories/files management

Basically help fms to create/remove/move files or directories.
Uses shutil high level python operations library and os python library.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 26/11/2016
"""

import os, shutil


class FileManager:

    def create_directory(self, directory_path):
        os.makedirs(directory_path)

    def create_file(self, file_path):
        with open(file_path, 'w') as stream:
            stream.write('[]')

    def copy_directory(self, source, destination):
        shutil.copytree(source, destination)

    def copy_file(self, file_name, source_dir, dest_dir):
        try:
            shutil.copyfile(
                source_dir + '/' + file_name,
                dest_dir + '/' + file_name
            )

        except:
            self.create_directory(dest_dir)
            self.copy_file(file_name, source_dir, dest_dir)

    def move_directory(self, source, destination):
        shutil.move(source, destination)

    def move_file(self, file_name, source_dir, dest_dir):
        try:
            shutil.move(
                source_dir + '/' + file_name,
                dest_dir + '/' + file_name
            )

        except:
            self.create_directory(dest_dir)
            self.move_file(file_name, source_dir, dest_dir)
