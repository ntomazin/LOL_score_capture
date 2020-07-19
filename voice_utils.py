from configparser import ConfigParser
import playsound


config = ConfigParser()
config.read("config.ini")

def play_sound(sound_type: str):
    playsound.playsound(config["voices"][sound_type], True)

