import os
import re

class Rename:    
    def __init__(self, path, node_origin, node_destin):
        self.root = path
        self._node_origin = node_origin
        self._node_destin = node_destin

    def rename(self):
        with  os.scandir(self.root) as items:
            for item in items:
               if item.is_dir():
                   self.search_in_subdirectory(item.path)

    # method recursive
    def search_in_subdirectory(self, directory):
        with  os.scandir(directory) as items:
             for item in items:
                if item.is_dir() and item.name.upper() == "VUCEM":
                    self.search_NP(item.path)
                elif self.is_NP_file(item.name):
                    self.overwrite_file(item.path)

    def search_NP(self, directory):        
        with os.scandir(directory) as files:
            for file in files:
                if self.is_NP_file(file.name):
                    self.overwrite_file(file.path)

    def overwrite_file(self, path):
        # print(path)
        if os.path.exists(path):    
            read_file = ""
            with open(path, "r", encoding="utf-8") as file:
                read_file = file.read()  
        read_file = re.sub(self._node_origin, self._node_destin, read_file)
        with open(path, "w", encoding="utf-8") as file:
            file.write(read_file)
            #print("Destinos de: ", self._node_origin, self._node_destin)

    def is_NP_file(self, filename):
        search = re.search(".*?NP\.xml", filename)
        return True if search is not None else False