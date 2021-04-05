import wave
import codecs
import struct
import librosa
import soundfile as sf
from os import path
from pydub import AudioSegment


def format():
    #opening files
    # files                                                                         
    src = "source/test.mp3"
    dst = "source/test1.wav"

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav") 
    x,_ = librosa.load("source/test.wav", sr=44100)
    sf.write("source/use.wav", x, 44100)
    input_file = wave.open(r"source/test.wav", 'rb')