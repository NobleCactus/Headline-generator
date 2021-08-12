# Andrew Eppinger
# OSU CS 361 Software Engineering I
# Summer 2021
# Headline Generator

import random
from flask import Flask

header = "Headline Generator"
intro = "Welcome to the Headline Generator app! Simply click the" \
        " 'Generate Headline' button to have a headline appear next to the" \
        "button. Clicking the button again will replace the existing headline," \
        "but you can revert to the previous headline by clicking the <--" \
        "buttons next to the generate buttons."

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

app = Flask(__name__)

@app.route('/')
    def homepage():
    return ""
    <h1>Hello heroku</h1>


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)