import pytest
from project import standardize_sentence, generate_phrases

def test_standardize_sentence():
    sentence = "heres an example sentence!"
    expected = "here's an example sentence"
    result = standardize_sentence(sentence)
    assert result == expected

def test_generate_phrases():
    words = 'this is a test'
    expected = [
        ['this', 'is', 'a', 'test'],
        ['this', 'is', 'a test'],
        ['this', 'is', 'a', 'test'],
        ['this', 'is a', 'test'],
        ['this', 'is a test'],
        ['this', 'is', 'a', 'test'],
        ['this', 'is', 'a test'],
        ['this', 'is', 'a', 'test'],
        ['this is', 'a', 'test'],
        ['this is', 'a test'],
        ['this is', 'a', 'test'],
        ['this is a', 'test'],
        ['this is a test'],
        ['this', 'is', 'a', 'test'],
        ['this', 'is', 'a test'],
        ['this', 'is', 'a', 'test'],
        ['this', 'is a', 'test'],
        ['this', 'is a test'],
        ['this', 'is', 'a', 'test'],
        ['this', 'is', 'a test'],
        ['this', 'is', 'a', 'test']
    ]
    result = generate_phrases(words)
    assert result == expected

if __name__ == "__main__":
    pytest.main()
