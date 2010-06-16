from silcc.lib.capnormalizer import capitalization_type, CapType

data = (
    ('What Is The Type', CapType.ALLCAPS),
    ('Adlevo Capital Wants To Invest $52 Million Into African Tech Businesses', CapType.ALLCAPS),
    ('SwiftRiver 101 at the iHub', CapType.REGULAR),
)

def test_cap_type():
    for x in data:
        assert capitalization_type(x[0]) == x[1]
