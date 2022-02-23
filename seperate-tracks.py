import librosa
import soundfile as sf


def run():
    
    filename = input("please enter a file name:")
    
    #cfile = convert(inputfile=filename, outputname=filename)
    
    # load converted WAV file
    y, sr = librosa.load(filename)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    print(f"Tempo: {tempo}")
    
    timestamps = librosa.frames_to_time(beats, sr=sr)
    print(timestamps)


    # Apply Short Time Fourier Transform
    D = librosa.stft(y)

    D_harmonic, D_percussive = librosa.decompose.hpss(D)
    y_harmonic = librosa.istft(D_harmonic, length=len(y))
    y_percussive = librosa.istft(D_percussive, length=len(y))
    
    # Write out audio as 24bit PCM WAV
    sf.write("percussive.wav", y_percussive, sr, subtype='PCM_24')
    sf.write("harmonics.wav", y_harmonic, sr, subtype='PCM_24')
    
    print("Done")

if __name__=='__main__':
    run()