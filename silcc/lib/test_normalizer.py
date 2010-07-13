import csv
from silcc.lib.normalizer import Normalizer

def test_normalizer():
    n = Normalizer()
    result = n.normalizer('This Is A Sure Example Of All Caps')
    assert result == 'this is a sure example of all caps'

    result = n.normalizer('LET US SHOUT SOME MORE. PLAY HARD. U.S.A')
    assert result == 'let us shout some more. play hard. U.S.A'
    
    result = n.normalizer('a very simple example of a lower case sentence')
    assert result == 'a very simple example of a lower case sentence'
    
    #result = n.normalizer('LET US SHOUT SOME MORE. PLAY HARD. NASA U.S.A')
    #assert result == 'Let us shout some more. Play hard. NASA U.S.A'
    
    #result = n.normalizer('LET US SHOUT SOME MORE. PLAY HARD. U.S.A BRAZIL')
    #assert result == 'Let us shout some more. Play hard. U.S.A Brazil'
