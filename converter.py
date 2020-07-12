from pydub import AudioSegment
import os

def convert():
	    sound = AudioSegment.from_mp3(os.path.expanduser("~/Downloads/audio.mp3"))
	    sound.export(os.path.expanduser("~/Downloads/audio.wav", format="wav")) 
