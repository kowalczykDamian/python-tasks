from collections import Counter

def hack_calculator(hack):
    valid_letters = {'a': 1, 'b': 2, 'c': 3}

    # check if hack string contains invalid letters
    if not set(hack).issubset(valid_letters):
        return 0

    # count bonus points for special phrases
    bonus = 20 * hack.count('baa') + 10 * (hack.count('ba') - hack.count('baa'))

    # count the number of occurrences of each letter in hack string
    num_of_occurrences = Counter(hack)

    # sum hack power | where sum of numbers from 0 to N is N(N+1)/2
    sum = 0
    for letter, power in valid_letters.items():
        sum += (num_of_occurrences[letter] * (num_of_occurrences[letter] + 1) / 2) * power

    return bonus + sum
