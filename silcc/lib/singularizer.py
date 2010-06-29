import re
import sys

from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()
rules = (

      # Specific rules for words which can't be handeled by below mentioned generic rules or the lemmetizer 
    (r'movies\b', 'movie'),
    (r'series\b', 'series'),
    (r'scissors\b', 'scissors'),
    (r'clothes\b', 'cloth'),
    (r'theses\b', 'thesis'),
    (r'indices\b', 'index'),
    (r'knives\b', 'knife'),
    (r'lives\b', 'life'),
    (r'thieves\b', 'thief'),
    (r'fungi\b', 'fungus'),
    
    # (r'women\b', 'woman'),
    # (r'\bmen\b', 'man'),
    # (r'sheep\b', 'sheep'),
    # (r'goose\b', 'geese'),     // Should have been geese ==> goose 
    # (r'pass\b', 'pass'),
    (r'radii\b', 'radius'),
    (r'(.*)ii\b', r'\1us'),
    (r'(.*)ies\b', r'\1y'),
    (r'(.*(ch|x|o|s))es', r'\1'),             #Should take care of words like beaches etc
    # (r'(.*?[^s])s\b', r'\1'),		      #DNS, Mars, Stars etc fix
    
  
    
)

compiled_rules = []
for r in rules:
    compiled_rule = (re.compile(r[0], re.IGNORECASE), r[1])
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
    # If none of our own rules hit fall back to NLTK lemmatizer
    return lmtzr.lemmatize(t)


if __name__ == '__main__':
    text = sys.argv[1]
    tokens = text.split()
    for token in tokens:
        print '%s ==> %s' % (token, singularize(token))




        






