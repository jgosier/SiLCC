import csv
from silcc.lib.normalizer import Normalizer

def test_normalizer():
    n = Normalizer()
    result = n.normalizer('This Is A Sure Example Of All Caps')
    assert result == 'This is a sure example of all caps'
