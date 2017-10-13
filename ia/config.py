import configparser
import re

class Config:
    """This class provides access to the global configuration"""
    config = configparser.ConfigParser()

    def __init__(self):
        self.config.read('config.ini')

    def get_video_path(self):
        return self.config['GLOBAL']['videoSaveDir']

    def get_image_path(self):
        return self.config['GLOBAL']['imageSaveDir']

    def get_cameras(self):
        cameras = {}
        for section in self.config.sections():
            if re.match('CAMERA_(.*)', section) is not None:
                cameras[section] = self.config.items(section)
        return cameras

    def get_camera_option(self, camera, option):
        return self.config.get(camera, option)

    def get_global_option(self, option):
        return self.config.get('GLOBAL', option)