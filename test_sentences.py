from sentences import get_determiner, get_noun, get_preposition, get_verb, get_prepositional_phrase, get_sentence
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single noun.

    single_noun = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(10):

        # Call the get_noun function which
        # should return a single determiner.
        noun = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_determiners list.
        assert noun in single_noun

    # 2. Test the plural noun.

    plural_noun = [ "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(10):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_noun function which
        # should return a plural determiner.
        noun  = get_noun (quantity)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_noun list.
        assert noun  in plural_noun 

def test_get_verb():
    # test the past tense verbs
    past_tense = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
     # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        tense = "past"

         # Call the get_verb function which
        # should return a verb in past tense.
        verb = get_verb(_, tense)

        # Verify that the word returned from get_verb
        # is one of the verb in the past_tense list.
        assert verb in past_tense

    # test the present tense one verbs
    present_tense_1 = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        tense = "present"

        # Call the get_verb function which
        # should return a verb in present tense.
        verb = get_verb(1, tense)

        # Verify that the word returned from get_verb
        # is one of the verb in the present_tense_1 list.
        assert verb in present_tense_1

    # test the present tense two verbs
    present_tense_2 = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):

        # variable verb conjugation
        tense = "present"

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_verb function which
        # should return a verb in present tense.
        verb = get_verb(quantity, tense)

        # Verify that the word returned from get_verb
        # is one of the verb in the present_tense_2 list.
        assert verb in present_tense_2

     # test the future tense  verbs
    future_tense = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):
        
        # variable verb conjugation
        tense = "future"

        # Call the get_verb function which
        # should return a verb in present tense.
        verb = get_verb(_, tense)

        # Verify that the word returned from get_verb
        # is one of the verb in the present_tense_2 list.
        assert verb in future_tense

def test_get_preposition():
    # Test the preposition
    prepositions = ["about", "above", "across", "after", "along",
                     "around", "at", "before", "behind", "below",
                     "beyond", "by", "despite", "except", "for",
                     "from", "in", "into", "near", "of",
                     "off", "on", "onto", "out", "over",
                     "past", "to", "under", "with", "without"]
     # This loop will repeat the statements inside it 10 times.
    for _ in range(30):

        # Call the get_preposition function which
        # should return a preposition.
        preposition = get_preposition()

        # Verify that the word returned from get_verb
        # is one of the verb in the present_tense_2 list.
        assert preposition in prepositions

def test_get_prepositional_phrase():
    # Test the prepositional phrase returned from get_prepositional_phrase.
    prepositional_phrase = get_prepositional_phrase(1).split(" ")
    assert len(prepositional_phrase) == 3
  
def test_get_sentence():
    # Test sentence returned from get_sentence.

    # list that determines the verb conjugation.
    tenses = ["past", "present", "future"]

    # This loop will repeat the statements inside it 10 times.
    for _ in range(10):
        tense = random.choice(tenses)

        # Call the get_sentence function with split method which
        # should return a list of words.
        sentence = get_sentence(_, tense).split(" ")

        # Verify that the length of list generate equal to 6.
        assert len(sentence) >= 6

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])