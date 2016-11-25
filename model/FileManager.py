""" Directories/files management

Basically help fms to create/remove/move files or directories.
Uses shutil high level python operations library and os python library.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 26/11/2016
"""

import os, shutil


class FileManager:

    def __init__(self, home_directory):
        self.__home_directory = home_directory

    def create_directory(self, directory_name, directory_path=''):
        if directory_path is '':
            os.makedirs(self.__home_directory + '/' + directory_name)
        else:
            os.makedirs(
                self.__home_directory + '/' + directory_path + '/'
                + directory_name
            )

    def create_file(self, file_name, file_path=''):
        if file_path is '':
            open(self.__home_directory + '/' + file_name)
        else:
            open(
                self.__home_directory + '/' + file_path + '/' + file_name
            ).close()

    def copy_directory(self, source, destination):
        shutil.copytree(
            self.__home_directory + '/' + source,
            self.__home_directory + '/' + destination
        )

    def copy_file(self, file_name, source_dir, dest_dir):
        try:
            shutil.copyfile(
                self.__home_directory + '/' + source_dir + '/' + file_name,
                self.__home_directory + '/' + dest_dir + '/' + file_name
            )

        except:
            self.create_directory(dest_dir)
            self.copy_file(file_name, source_dir, dest_dir)

    def move_directory(self, source, destination):
        shutil.move(
            self.__home_directory + '/' + source,
            self.__home_directory + '/' + destination
        )

    def move_file(self, file_name, source_dir, dest_dir):
        try:
            shutil.move(
                self.__home_directory + '/' + source_dir + '/' + file_name,
                self.__home_directory + '/' + dest_dir + '/' + file_name
            )

        except:
            self.create_directory(dest_dir)
            self.move_file(file_name, source_dir, dest_dir)
