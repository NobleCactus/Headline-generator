# Andrew Eppinger
# OSU CS 361 Software Engineering I
# Summer 2021
# Headline Generator

import random

# Complete list of nouns for the noun generator
noun_dictionary_all = {0: "Man", 1: "Woman", 2: "Child", 3: "Mayor",
                    4: "Policeman", 5: "Firefighter", 6: "Doctor", 7: "Lawyer",
                    8: "Teacher", 9: "Husband", 10: "Wife", 11: "City Hall",
                    12: "Bank", 13: "Supermarket", 14: "Church",
                    15: "Restaurant", 16: "Concert Hall", 17: "Golf Course",
                    18: "Firehouse", 19: "Police Station", 20: "Zoo",
                    21: "Dog", 22: "Cat", 23: "Mouse", 24: "Plane", 25: "Car",
                    26: "Bus", 27: "Company", 28: "Computer", 29: "Race"}

# Complete list of verbs for the verb generator
verb_dictionary_all = {0: "bites", 1: "abandons", 2: "accuses",
                          3: "threatens", 4: "wins over", 5: "loses",
                          6: "sues", 7: "adopts", 8: "robs", 9: "burns down",
                          10: "opens", 11: "closes", 12: "saves",
                          13: "condemns", 14: "buys", 15: "sells"}

# Nouns are broken down into person, place, and thing. Enables easier addition
# of more nouns later. Verbs are assigned based on person, place, or thing.
noun_dictionary_person = {0: "Man", 1: "Woman", 2: "Child", 3: "Mayor",
                    4: "Policeman", 5: "Firefighter", 6: "Doctor", 7: "Lawyer",
                    8: "Teacher", 9: "Husband", 10: "Wife"}

noun_dictionary_place = {0: "City Hall", 1: "Bank", 2: "Supermarket",
                         3: "Church", 4: "Restaurant", 5: "Concert Hall",
                         6: "Golf Course", 7: "Firehouse",
                         8: "Police Station", 9: "Zoo"}

noun_dictionary_thing = {0: "Dog", 1: "Cat", 2: "Mouse", 3: "Plane", 4: "Car",
                         5: "Bus", 6: "Company", 7: "Computer", 8: "Race"}


verb_dictionary_person = {0: "bites", 1: "abandons", 2: "accuses",
                          3: "threatens", 4: "wins over", 5: "loses",
                          6: "sues", 7: "adopts"}

verb_dictionary_place = {0: "robs", 1: "burns down", 2: "opens", 3: "closes",
                        4: "saves", 5: "condemns", 6: "buys", 7: "sells"}


def generate_headline():
    person_place_or_thing = random.randint(1,2)
    if person_place_or_thing == 1:
        noun_1 = noun_dictionary_person[random.randint(0, (len(noun_dictionary_person)-1))]
        verb = verb_dictionary_person[random.randint(0, (len(verb_dictionary_person)-1))]
        noun_2 = noun_dictionary_person[random.randint(0, (len(noun_dictionary_person)-1))]

    elif person_place_or_thing == 2:
        noun_1 = noun_dictionary_person[random.randint(0, (len(noun_dictionary_person)-1))]
        verb = verb_dictionary_place[random.randint(0, (len(verb_dictionary_place)-1))]
        noun_2 = noun_dictionary_place[random.randint(0, (len(noun_dictionary_place)-1))]
   # else:
       # noun_1 = noun_dictionary_thing[random.randint(0, (len(noun_dictionary_thing)-1))]
       # verb = verb_dictionary_person[random.randint(0, (len(verb_dictionary_person)-1))]



    return noun_1 + " " + verb + " " + noun_2

def generate_noun():
    noun = noun_dictionary_all[random.randint(0, (len(noun_dictionary_all.keys())-1))]
    return noun

def generate_verb():
    verb = verb_dictionary_all[random.randint(0, (len(verb_dictionary_all.keys())-1))]
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
