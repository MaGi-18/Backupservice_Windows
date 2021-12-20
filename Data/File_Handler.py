import os

class File_Handler():

    def is_File_exists(self, filePath:str) -> bool:

        return os.path.exists(filePath)