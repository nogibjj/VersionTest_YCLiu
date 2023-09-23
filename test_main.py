from main import shortenStr

def test_func():
    assert shortenStr("Hello world!", "Hello ") == "world!"

if __name__ == '__main__':
    test_func()
    pass