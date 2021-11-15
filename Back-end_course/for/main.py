from helpers import get_countries
import re


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """
def shortest_names(countries):
    # Variable to be returned
    shortest = [""]

    # Input check
    if not(len(countries) > 0 or type(countries) == "list"):
        return "Incorrect input!"

    # Length check & handling
    else:
        for c in countries:
            current_length_shortest = len(shortest[0])
            country_name_length = len(c)
            if(current_length_shortest == 0 or country_name_length < current_length_shortest):
                shortest = [c]
            elif(current_length_shortest == country_name_length):
                shortest.append(c)
            else:
                continue

    return shortest

def most_vowels(countries):
    # sorting key
    def sort_by_vowel(country_name):
        amount_of_vowels = 0

        for letter in country_name:
            is_vowel = re.search("[aAoOeEiIuU]", letter)
            if is_vowel:
                amount_of_vowels += 1
        
        return amount_of_vowels

    sorted_countries = sorted(countries, reverse=True, key=sort_by_vowel) 

    return sorted_countries[0:3]   

def alphabet_set(countries):

    #sort countries on name length for better chance of unique letters
    sorted_on_length = sorted(countries, reverse=True, key=len)

    #"Buckets" to store al unique letters and countries
    letters_processed = []
    countries_used = []
    
    for country_name in sorted_on_length:
        processed_letter_counter = 0

        for letter in country_name:
            is_letter = re.search("\w", letter)
            
            if is_letter:
                standardized_letter = letter.lower()
                if standardized_letter not in letters_processed:
                    letters_processed.append(standardized_letter)
                    processed_letter_counter += 1

        if processed_letter_counter > 0:
            countries_used.append(country_name)
        else:
            continue

    return countries_used


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()
    shortest_names(countries)
    most_vowels(countries)
    alphabet_set(countries)
    """ Write the calls to your functions here. """