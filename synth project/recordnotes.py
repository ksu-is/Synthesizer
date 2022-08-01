import numpy as np
import pygame as py
import scipy.io.wavfile as wav
from scipy.io.wavfile import write


sample_rate= 44100

def sine () :
    amplitude= 4096
    return(amplitude * np.sin)

def sawtooth(x) :
    return(x + np.pi) / np.pi % 2 - 1
    
def get_wave(freq, duration=0.6):
    amplitude = 4096
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)

    return wave
def get_piano_notes():
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B', 'b', 'C2', 'c2', 'D2', 'd2', 'E2', 'F2', 'f2', 'G2', 'g2', 'A2', 'a2', 'B2']
    base_freq = 261.63

    note_freqs = {octave[i]:base_freq*pow(2, (i/12)) for i in range(len(octave))}
    note_freqs[''] = 0.0

    return note_freqs

def get_song_data(music_notes):
    note_freqs = get_piano_notes()
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)

    return song.astype(np.int16)


def get_chord_data(chords):
    chords = chords.split('-')
    note_freqs = get_piano_notes()

    chord_data = []
    for chord in chords:
        data = sum([get_wave(note_freqs[note]) for note in list(chord)])
        chord_data.append(data)

    chord_data = np.concatenate(chord_data, axis = 0)

    return chord_data.astype(np.int16)

if __name__ == '__main__':
    #single notes, can have rest notes 
    music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C' 
    data = get_song_data(music_notes)
    data = data * (16300/np.max(data))
    write('twinklesaw2.wav', sample_rate, data.astype(np.int16))
    #chords, but trying rest notes results in error 
    chords = ''
    data = get_chord_data(chords)
    data = data * (16300/np.max(data))
    data = np.resize(data, (len(data)*5,))
    #write('stars.wav', sample_rate, data.astype(np.int32))
