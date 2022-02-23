import importlib
import subprocess
import os
import sys

python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')

def getDeps():
    subprocess.call([python_exe, "-m", "ensurepip"])
    doesExist()
    print("Dependencies Updated!")

def doesExist():
    if importlib.util.find_spec("soundfile") is None:
        subprocess.call([python_exe, "-m", "pip", "install", "soundfile"])
        print("Downloading Soundfile through pip...")
    if importlib.util.find_spec("librosa") is None:
        subprocess.call([python_exe, "-m", "pip", "install", "librosa"])
        print("Downloading librosa through pip...")
    else: 
        print("Required imports already installed.")

if __name__=='__main__':
    getDeps()