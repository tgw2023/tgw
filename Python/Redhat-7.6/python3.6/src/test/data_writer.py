# coding=utf-8

import sys
import os
from threading import Lock

file_locker = Lock()

class DataWriter():
    def __init__(self, dir, file_name):
        self.file_path = dir + "/" + file_name
        try:
            file_locker.acquire()

            if(os.path.exists(dir) == False):
                os.makedirs(dir)
            elif(os.path.exists(self.file_path)):
                os.remove(self.file_path)
            self.file_writer = open(self.file_path, "w+", encoding='utf-8')
            
            file_locker.release()

        except Exception as error:
            print(error)
            pass
    
    def WriteTitle(self,title):
        try:
            self.file_writer.write(title)
            self.file_writer.flush()
        except Exception as error:
            print(error)
            pass
    
    def WriteData(self, data):
        try:
            self.file_writer.write(data)
            self.file_writer.flush()
        except Exception as error:
            print(error)
            pass

    def ReOpen(self):
        try:
            self.Close()
            self.file_writer = open(self.file_path, "w+", encoding='utf-8')
        except Exception as error:
            print(error)
            pass

    def Close(self):
        try:
            self.file_writer.close()
        except Exception as error:
            print(error)
            pass

