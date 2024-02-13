import serial
import time
import numpy as np
from synthesizer import Player, Synthesizer, Waveform

ser = serial.Serial('COM4', 9600)

player = Player()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

player.open_stream()

def generate_chord(x, y, z):
    frequency_x = 100 + x * 10 
    frequency_y = 100 + y * 10 
    frequency_z = 100 + z * 10 

    chord_notes = [frequency_x, frequency_y, frequency_z]  
    
    return chord_notes

while True:
    if ser.readable():
        data = ser.readline().decode().strip()
        if data:
            parts = data.split(',')
            if len(parts) == 3:
                x, y, z = map(float, parts)
                print("X:", x, "Y:", y, "Z:", z)
                
                chord_to_play = generate_chord(x, y, z)

                player.play_wave(synthesizer.generate_chord(chord_to_play, 1.0))
            else:
                print("Received data does not contain three values:", data)


