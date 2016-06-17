

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
    
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def ask_Customer():
    
    answer1 = input(questions["strong"])
    answer2 = input(questions["salty"])
    answer3 = input(questions["bitter"])
    answer4 = input(questions["sweet"])
    answer5 = input(questions["fruity"])
    
    convert_to_Bool = {"yes": True, "no" : False}
    
    bool_answer1 = convert_to_Bool[answer1]
    bool_answer2 = convert_to_Bool[answer2]
    bool_answer3 = convert_to_Bool[answer3]
    bool_answer4 = convert_to_Bool[answer4]
    bool_answer5 = convert_to_Bool[answer5]
    
    preferences = {
        "strong" : bool_answer1,
        "salty" : bool_answer2,
        "bitter" : bool_answer3,
        "sweet" : bool_answer4,
        "fruity" : bool_answer5,
        }
    return preferences
    

def drink_construction(preferences):
    import random
    drink = [ ]
    for key,value in preferences.items():
        if value == True:
            drink.append(random.choice(ingredients[key]))
            
    return drink

def drink_name():
    import random
    adjective = ["salty", "sweet", "fluffy", "magnificent"]
    noun = ["dog", "cat", "chichilla", "sea-turtle"]
    print("The name of your drink is {}".format(random.choice(adjective)) + "-{}".format(random.choice(noun)))
    
    
def main():
    find_preferences = ask_Customer()
    make_drink = drink_construction(find_preferences)
    print("One drink coming up!")
    drink_name()
    print("The recipe will be:  {}".format(make_drink))
    
if __name__ == "__main__":
    main()
    
   
    
    
    
    
