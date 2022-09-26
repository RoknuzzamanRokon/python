import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration = 20

recording = sd.rec(int(duration * freq), samplerate = freq, channels = 2)

sd.wait()


write("recording0.wav", freq, recording)
  
wv.write("recording1.wav", recording, freq, sampwidth=2)
    

from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_wav('recording1.wav')
play(sound)