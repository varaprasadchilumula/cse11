import random


def main():
    quantity_1 = 1
    quantity_2 = 2
    tense = ["past", "present", "future"]

    # single past sentence
    determiner_1 = get_determiner(quantity_1)
    noun_1 = get_noun(quantity_1)
    verb_1 = get_verb(quantity_1, tense[0])
    sentence_1 = f"{determiner_1.capitalize()} {noun_1} {verb_1}"
    print(sentence_1)

    # single present sentence
    determiner_2 = get_determiner(quantity_1)
    noun_2 = get_noun(quantity_1)
    verb_2 = get_verb(quantity_1, tense[1])
    sentence_2 = f"{determiner_2.capitalize()} {noun_2} {verb_2}"
    print(sentence_2)

    # single future
    determiner_3 = get_determiner(quantity_1)
    noun_3 = get_noun(quantity_1)
    verb_3 = get_verb(quantity_1, tense[2])
    sentence_3 = f"{determiner_3.capitalize()} {noun_3} {verb_3}"
    print(sentence_3)

    # plural past
    determiner_4 = get_determiner(quantity_2)
    noun_4 = get_noun(quantity_2)
    verb_4 = get_verb(quantity_2, tense[0])
    sentence_4 = f"{determiner_4.capitalize()} {noun_4} {verb_4}"
    print(sentence_4)

    # plural present
    determiner_5 = get_determiner(quantity_2)
    noun_5 = get_noun(quantity_2)
    verb_5 = get_verb(quantity_2, tense[1])
    sentence_5 = f"{determiner_5.capitalize()} {noun_5} {verb_5}"
    print(sentence_5)

    # plural future
    determiner_6 = get_determiner(quantity_2)
    noun_6 = get_noun(quantity_2)
    verb_6 = get_verb(quantity_2, tense[2])
    sentence_6 = f"{determiner_6.capitalize()} {noun_6} {verb_6}"
    print(sentence_6)


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    # print(word)
    return word

# get_determiner(2)


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]

    word = random.choice(words)
    # print(word)
    return word
# get_noun(2)


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    verb = random.choice(verbs)
    # print(verb)
    return verb


main()
