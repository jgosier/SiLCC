from silcc.lib.singularizer import singularize

def test_singularizer():
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
