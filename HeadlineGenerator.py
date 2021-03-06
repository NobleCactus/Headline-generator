# Andrew Eppinger
# OSU CS 361 Software Engineering I
# Summer 2021
# Headline Generator

import random
import requests

header = "Headline Generator"
intro = "Welcome to the Headline Generator app! Simply click the" \
        " 'Generate Headline' button to have a headline appear next to the" \
        "button. Clicking the button again will replace the existing headline," \
        "but you can revert to the previous headline by clicking the <--" \
        "buttons next to the generate buttons. Keep in mind that you can only" \
        "revert to the MOST RECENT headline, noun, or verb, you cannot revert" \
        "back farther than that. The 'Generate Anagram' button will use an " \
        "anagram generator to try and get an anagram for each word in the" \
        "currently generated headline. It will display 'No anagram available'" \
        "if no anagram exists for any word in the headline"

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
                         5: "Bus", 6: "Company", 7: "Computer"}


verb_dictionary_person = {0: "bites", 1: "abandons", 2: "accuses",
                          3: "threatens", 4: "wins over", 5: "loses",
                          6: "sues", 7: "adopts"}

verb_dictionary_place = {0: "robs", 1: "burns down", 2: "opens", 3: "closes",
                         4: "saves", 5: "condemns", 6: "buys", 7: "sells"}

verb_dictionary_thing = {0: "returned to rightful owner",
                         1: "catches fire, several injured",
                         2: "survives despite long odds",
                         3: "returns from space", 4: "saved from destruction",
                         5: "predicts disaster", 6: "predicts success",
                         7: "sells for record amount",
                         8: "bought for record amount"}

# All are set to None to facilitate the previous button mechanics.
headline = None
prev_headline = None
prev_noun = None
prev_verb = None

# Generates a random integer 1-3. Generated int determines the noun and verb
# dictionaries that are selected to create each headline.
def generate_headline():
    person_place_or_thing = random.randint(1, 3)
    if person_place_or_thing == 1:
        noun_1 = noun_dictionary_person[random.randint(0, (len(noun_dictionary_person)-1))]
        verb = verb_dictionary_person[random.randint(0, (len(verb_dictionary_person)-1))]
        noun_2 = noun_dictionary_person[random.randint(0, (len(noun_dictionary_person)-1))]
        headline = noun_1 + " " + verb + " " + noun_2
        return headline
    elif person_place_or_thing == 2:
        noun_1 = noun_dictionary_person[random.randint(0, (len(noun_dictionary_person)-1))]
        verb = verb_dictionary_place[random.randint(0, (len(verb_dictionary_place)-1))]
        noun_2 = noun_dictionary_place[random.randint(0, (len(noun_dictionary_place)-1))]
        headline = noun_1 + " " + verb + " " + noun_2
        return headline
    else:
        noun_1 = noun_dictionary_thing[random.randint(0, (len(noun_dictionary_thing)-1))]
        verb = verb_dictionary_thing[random.randint(0, (len(verb_dictionary_thing)-1))]
        headline = noun_1 + " " + verb
        return headline


def generate_noun():
    noun = noun_dictionary_all[random.randint(0, (len(noun_dictionary_all.keys())-1))]
    return noun

def generate_verb():
    verb = verb_dictionary_all[random.randint(0, (len(verb_dictionary_all.keys())-1))]
    return verb

def call_anagram(headline):
    if headline == None:
        return "Generate a headline first!"
    headline_words = headline.split(" ")
    out = ''
    for word in headline_words:
        payload = {"text": headline}
        URL = "http://flip3.engr.oregonstate.edu:3480/search/"
        URL += word
        response = requests.get(URL, params=payload)
        text_response = response.text
        out += text_response + " "
    out = out[0:-1]
    print(out)
    if out == headline.lower():
        out = 'No anagram available for this headline. Sorry!'
    return out

import PySimpleGUI as sg

margins = (100, 100)

# Code below is used for the layout of the GUI.
gen_headline_button = sg.B("Click here to generate a headline!", size=(25,0))
gen_headline_out = sg.T("Generated headline will appear here!", pad=(50,0), key="hl")
previous_headline = sg.B("<--", size=(3,0), key="prev_hl")
gen_noun_button = sg.B("Click here to generate a noun!", size=(25,0))
gen_noun_out = sg.T("Generated noun will appear here!", pad=(50,0), key="noun")
previous_noun = sg.B("<--", size=(3,0), key="prev_noun")
gen_verb_button = sg.B("Click here to generate a verb!", size=(25,0))
gen_verb_out = sg.T("Generated verb will appear here!", pad=(50,0), key="verb")
previous_verb = sg.B("<--", size=(3,0), key="prev_verb")
gen_anagram_button = sg.B("Click here to generate an anagram!", size=(25,0))
gen_anagram_out = sg.T("Generated anagram will appear here!", pad=(93,0), key="ana")

layout = [[sg.T(header, justification="c", pad=(225,0),)], [sg.T(intro, size=(75,0), justification='c')],
         [previous_headline, gen_headline_button, gen_headline_out],
         [previous_noun, gen_noun_button, gen_noun_out],
         [previous_verb, gen_verb_button, gen_verb_out], [gen_anagram_button, gen_anagram_out]],\
         [sg.Multiline(size=(75,20))],[sg.B("Exit Program")]


window = sg.Window("Headline Generator", layout, margins=margins)
while True:
    event, values = window.read()
    if event == "Click here to generate a headline!":
        if prev_headline == None:
            window["hl"].update(generate_headline())
            headline = window["hl"].get()
            prev_headline = window["hl"].get()
        else:
            prev_headline = window["hl"].get()
            window["hl"].update(generate_headline())
            headline = window["hl"].get()

    elif event == "Click here to generate a noun!":
        if prev_noun == None:
            window["noun"].update(generate_noun())
            prev_noun = window["noun"].get()
        else:
            prev_noun = window["noun"].get()
            window["noun"].update(generate_noun())

    elif event == "Click here to generate a verb!":
        if prev_verb == None:
            window["verb"].update(generate_verb())
            prev_verb = window["verb"].get()
        else:
            prev_verb = window["verb"].get()
            window["verb"].update(generate_verb())


    elif event == "Click here to generate an anagram!":
        window["ana"].update(call_anagram(headline))

#Previous button GUI update mechanics.
    elif event == "prev_hl":
        window["hl"].update(prev_headline)
    elif event == "prev_noun":
        window["noun"].update(prev_noun)
    elif event == "prev_verb":
        window["verb"].update(prev_verb)

#Exit and "x" buttons will close the GUI without an error.
    elif event == "Exit Program":
        break
    elif event == sg.WIN_CLOSED:
        break
