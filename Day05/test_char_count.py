import char_count_pack
import pytest

@pytest.mark.parametrize("text, expected", 
                         [("Hello, World!", 13),
                          ("Fight\nor\nflight", 15),
                          ("Words count less than\nactions!", 30)])

def test_char_count(text, expected):
    result = char_count_pack.char_count(text)
    assert result == expected

@pytest.mark.parametrize("text, expected", 
                         [("Hello, World!", 1),
                          ("Fight\nor\nflight", 3),
                          ("Words count less than\nactions!", 2)])
    
def test_line_count(text, expected):
    result = char_count_pack.line_count(text)
    assert result == expected

@pytest.mark.parametrize("text, expected", 
                         [("Hello, World!", 2),
                          ("Fight\nor\nflight", 3),
                          ("Words count less than\nactions!", 5)])

def test_word_count(text, expected):
    result = char_count_pack.word_count(text)
    assert result == expected