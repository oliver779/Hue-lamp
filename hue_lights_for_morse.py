from phue import Bridge
from ipaddress2 import bridge_ip_address
import pprint
import time
import json
import os
import numpy as np
"""This code aims at turning on/off the hue light. Apart from turning on and off, you can change the color of the light and 
its brightness. You can also play around with a simple morse code, where the user inputs a sentence, and the light will play it in morse
code.
"""
b = Bridge(bridge_ip_address)
b.connect()
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'mor.json')
with open(my_file) as f:
    m_data = json.load(f)

with open('output.txt', 'wt') as out:
    pprint.pprint(b.get_api(), stream=out)

def dot():
    b.set_light(2,'on', True)
    time.sleep(1)
    b.set_light(2,'on', False)
    time.sleep(1)
    b.set_light(2,'on', False)

def line():
    b.set_light(2,'on', True)
    time.sleep(3)
    b.set_light(2,'on', False)
    time.sleep(1)
    b.set_light(2,'on', False)

def space_between_letters(): 
    b.set_light(2,'on', False)
    time.sleep(2)
    b.set_light(2,'on', False)

def space_between_words(): 
    b.set_light(2,'on', False)
    time.sleep(5)
    b.set_light(2,'on', False)


def turn_on_off():
    input5 = int(input("Please give a number between 0 and 65000, which will give the lamp a color "))
    input6 = int(input("Please give a number between 0 and 254, which will give the lamp a color "))
    input3 = input("Would you like to turn on the lamp? (y/n)")
    if input3 == "y":
        command =  {'on' : True, 'bri' : input6, 'hue': input5}
        b.set_light(2,command)
    if input3 =="n":
       b.set_light(2,'on', False)
    input4 = input("Would you like to play with morse code? (y/n)")
    if input4 == "y":
        return print("ok")
    else:
        exit()
turn_on_off()

morse_array = []
def sentence_to_morse():
    sentence_array = []
    breaker = '|'
    input_sentence = input("Enter sentence to be changed to morse code:")
    sentence_array.append(input_sentence)
    for i in sentence_array:
        for element in i:
            if element == ' ':
                morse_array.append(breaker)
                continue
            morse_array.append(m_data[element])
    return sentence_array, morse_array, print("The sentence from input is:",sentence_array, "which after transforming to morse code, looks like this:", morse_array)
sentence_to_morse()

def morse_hue():
    input2 = input("Would you like to play your sentence on the hue lamp? (y/n)")
    if input2 == "y":
        for i in morse_array:
            # space_between_letters
            for element in i:
                if element == '^':
                    space_between_letters()
                if element == '*':
                    dot()
                if element == '-':
                    line()
                if element == '|':
                    space_between_words()
                print(element)   
    if input2 == "n":
        exit()
morse_hue()