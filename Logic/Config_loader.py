from Data import File_Handler
from config import Settings

class Config_loader():

    def __init__(self):
        self.__fileHandler = File_Handler.File_Handler()

    def get_ProcessConfig_data(self) -> dict:
        """
        Ist die Config-Datei vorhanden?
            ja -> Datei auslesen
            nein -> Default-Datei anlegen und Meldung zurück
        """
        if not self.__fileHandler.is_File_exists(Settings.config_Filename):
            print("The process config file does not exist. Create a new one with default values.")
