import os
import re

class Rename:

    def __init__(self, path, node_origin, node_destin):
        self._count = 0
        self.root = path
        self._node_origin = node_origin
        self._node_destin = node_destin

    def rename(self):
        with  os.scandir(self.root) as items:
            for item in items:
               if item.is_dir():
                   self.search_in_subdirectory(item.path)

    def rename2(self, references):
        for reference in references:
            path = os.path.join(self.root,reference[0])
            if os.path.exists(os.path.join(path)):
                self.search_in_subdirectory(path)

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

        if re.search(self._node_origin, read_file) is not None:
            read_file = re.sub(self._node_origin, self._node_destin, read_file)
            with open(path, "w", encoding="utf-8") as file:
                self._count += 1
                file.write(read_file)
            #print("Destinos de: ", self._node_origin, self._node_destin)

    def is_NP_file(self, filename):
        search = re.search(".*?NP\.xml", filename)
        return True if search is not None else False

    def get_count(self):
        return self._count


