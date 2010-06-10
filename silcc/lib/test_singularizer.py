import csv

from silcc.lib.singularizer import singularize

def test_singularizer():
    assert singularize('series') == 'series'
    assert singularize('women') == 'woman'
    assert singularize('radii') == 'radius'
    assert singularize('octopii') == 'octopus'
    assert singularize('virii') == 'virus'
    assert singularize('fish') == 'fish'
    assert singularize('properties') == 'property'
    assert singularize('drapes') == 'drape'
    assert singularize('types') == 'type'
    assert singularize('pass') == 'pass'
    assert singularize('balls') == 'ball'
    assert singularize('men')  == 'man'

def test_singularizer_abraxas_tags():
    """This is not a true test, it just
    outputs the singularize result on 
    Abraxas tags in order to bootstrap the
    singularizer rules"""
    reader = csv.reader(open('../../data/tests/abraxas_tags.csv'))
    for line in reader:
        print '%s ==> %s' % (line[2], singularize(line[2]))
