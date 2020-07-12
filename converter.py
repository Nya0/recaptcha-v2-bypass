from pydub import AudioSegment

def convert():
	    sound = AudioSegment.from_mp3("~/Downloads/audio.mp3")
	    sound.export("~/Downloads/audio.wav", format="wav") 
