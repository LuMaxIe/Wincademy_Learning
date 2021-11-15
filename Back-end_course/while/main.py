from helpers import random_koala_fact
import re

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'  

def unique_koala_facts(num_of_facts):
    facts_list = []
    i = 0
    while i <= num_of_facts:
        new_fact = random_koala_fact()
        if new_fact not in facts_list:
            facts_list.append(new_fact)
        i += 1    
    return facts_list

def num_joey_facts():
    fact_to_count = random_koala_fact()
    joey_count = set({})
    i = 0
    while i < 10:
        new_fact = random_koala_fact()
        if "joey" in new_fact:
            joey_count.add(new_fact)
        if new_fact == fact_to_count:
            i += 1
        else:
            new_fact = random_koala_fact()

    return len(list(joey_count))

def koala_weight():
    search_terms = ["kilograms", "kilogram", "kilos", "kg", "kilo's"]
    kilos = 0

    while kilos == 0:
        fact_to_search = random_koala_fact()
        for term in search_terms:
            if term in fact_to_search:
                search_regex = r"(\d{1,10}|\d{1,10}.\d{1,10})(?=" + term + r")|(?<=" + term + r")(\d{1,10}|\d{1,10}.\d{1,10})"
                found_term = re.search(search_regex, fact_to_search, flags=0)
                if found_term != None:
                    kilos = int(found_term.group())
                else:
                    kilos = 0
                    fact_to_search = random_koala_fact()

    return "No weight fact found with these search terms" if kilos == 0 else kilos

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    unique_koala_facts()
    num_joey_facts()
    koala_weight()
    # print(random_koala_fact())
