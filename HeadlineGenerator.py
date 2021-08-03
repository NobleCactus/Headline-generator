# Andrew Eppinger
# OSU CS 361 Software Engineering I
# Summer 2021
# Headline Generator

import random

noun_dictionary = {0: "Man", 1: "Woman", 2: "Child", 3: "Mayor",
                    4: "Policeman", 5: "Firefighter", 6: "Doctor", 7: "Lawyer",
                    8: "Teacher", 9: "Husband", 10: "Wife", 11: "City Hall",
                    12: "Bank", 13: "Supermarket", 14: "Church",
                    15: "Restaurant", 16: "Concert Hall", 17: "Golf Course",
                    18: "Firehouse", 19: "Police Station", 20: "Zoo",
                    21: "Dog", 22: "Cat", 23: "Mouse", 24: "Plane", 25: "Car",
                    26: "Bus", 27: "Company", 28: "Computer", 29: "Race"}
verb_dictionary = {0: "bites", 1: "abandons", 2: "accuses", 3: "threatens",
                   4: "wins over", 5: "loses", 6: "sues", 7: "adopts"}


def generate_headline():

    noun_1 = noun_dictionary[random.randint(0, 10)]
    verb = verb_dictionary[random.randint(0, (len(verb_dictionary)-1))]
    noun_2 =  noun_dictionary[random.randint(0, (len(noun_dictionary)-1))]
    while noun_1 == noun_2:
        noun_2 = noun_dictionary[random.randint(0, (len(noun_dictionary)-1))]
    return noun_1 + " " + verb + " " + noun_2

def generate_noun():
    noun = noun_dictionary[random.randint(0, (len(noun_dictionary.keys())-1))]
    return noun

def generate_verb():
    verb = verb_dictionary[random.randint(0, (len(verb_dictionary.keys())-1))]
    return verb

import PySimpleGUI as sg

margins = (100, 100)
sz = (10, 10)

gen_headline_button = sg.B("Click here to generate a headline!", size=(25,0))
gen_headline_out = sg.T("Generated headline will appear here!", pad=(50,0), key="hl")
gen_noun_button = sg.B("Click here to generate a noun!", size=(25,0))
gen_noun_out = sg.T("Generated noun will appear here!", pad=(50,0), key="noun")
gen_verb_button = sg.B("Click here to generate a verb!", size=(25,0))
gen_verb_out = sg.T("Generated verb will appear here!", pad=(50,0), key="verb")
gen_anagram_button = sg.B("Click here to generate an anagram!", size=(25,0))
gen_anagram_out = sg.T("Generated anagram will appear here!", pad=(50,0), key="ana")
layout = [[gen_headline_button, gen_headline_out], [gen_noun_button, gen_noun_out],
          [gen_verb_button, gen_verb_out], [gen_anagram_button, gen_anagram_out]],\
         [sg.Multiline(size=(75,20))],[sg.B("Exit Program")]


window = sg.Window("Headline Generator", layout, margins=margins)
while True:
    event, values = window.read()
    gen_headline_out = sg.T("Horse")

    if event == "Click here to generate a headline!":
        window["hl"].update(generate_headline())
    elif event == "Click here to generate a noun!":
        window["noun"].update(generate_noun())
    elif event == "Click here to generate a verb!":
        window["verb"].update(generate_verb())
    elif event == "Exit Program":
        break
    elif event == sg.WIN_CLOSED:
        break
