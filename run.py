import itertools
import string

def generate_strings():
    with open('.wordlist.list', 'w') as f:
        seen_strings = set() # Keep track of generated strings
        for length in range(1, 100):
            for chars in itertools.product(string.printable, repeat=length):
                new_string = ''.join(chars)
                if new_string not in seen_strings:
                    f.write(new_string + '\n')
                    seen_strings.add(new_string)

generate_strings()

