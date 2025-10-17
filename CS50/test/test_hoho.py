
from hoho import hoho

def test_response():
    assert hoho("josh") == "Hello, josh"
    assert hoho() == "Hello, world baby"

def test_difname():
    for name in ["Dodo", "Wishs", "Bitchen"]:
        assert hoho(name) == f"Hello, {name}"