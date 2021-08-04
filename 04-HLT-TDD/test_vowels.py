from vowels import vowels

def test_vowels():
    assert vowels('fred')
    assert vowels('syzygy') == False
    assert vowels('rhythm') == False
    assert vowels('then')
    assert vowels('euoeae')
    