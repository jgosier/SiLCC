# -*- coding: utf-8 -*-
from silcc.lib.capnormalizer import capitalization_type, CapType

data = (
    ('this is an example of lower', CapType.LOWER),
    ('This is an example of regular', CapType.REGULAR),
    ('This Is An Example Of Allcaps', CapType.ALLCAPS),
    ('THIS IS AN EXAMPLE Of SHOUT', CapType.SHOUT),
    ('What Is The Type', CapType.ALLCAPS),
    ('Adlevo Capital Wants To Invest $52 Million Into African Tech Businesses', CapType.ALLCAPS),
    ('SwiftRiver 101 at the iHub', CapType.REGULAR),
    ('Alarena The Nigerian Matchmaker Is Now Your “Lovebase”', CapType.ALLCAPS),
    ("SA exporting manpower to Iraq", CapType.REGULAR),
    ("Student Skydiver dies in Gravity related incident", CapType.REGULAR)
)

def test_cap_type():
    for x in data:
        try:
            assert capitalization_type(x[0]) == x[1]
        except:
            print 'Error: %s' % x[0]
            print 'Result should be %s but got %s' % (x[1], capitalization_type(x[0]))
            raise


