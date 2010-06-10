import re
import sys

rules = (
    (r'sheep\b', 'sheep'),
    (r'goose\b', 'geese'),
    (r'pass\b', 'pass'),
    (r'radii\b', 'radius'),
    (r'(.*)ii\b', r'\1us'),
    (r'(.*)ies\b', r'\1y'),
    (r'(.*)s\b', r'\1'),
)

compiled_rules = []
for r in rules:
    compiled_rule = (re.compile(r[0]), r[1])
    compiled_rules.append(compiled_rule)

def singularize(t):
    """Given a plural form of an English word, 
    returns its singular form.
    It is assumed that by the time the singularizer
    is called prior processing has already determined
    that the word is a noun.
    
    >>> singualrize('octopii')
    > octopus
    """
    for r in compiled_rules:
        if r[0].match(t):
            return r[0].sub(r[1], t)
    return t

if __name__ == '__main__':
    text = sys.argv[1]
    tokens = text.split()
    for token in tokens:
        print '%s ==> %s' % (token, singularize(token))




        






