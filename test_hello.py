from hello import hello

def test_default():
    assert hello("Asik") == "hello, Asik"
    
    
def test_argument():
    assert hello() == "hello, world"
