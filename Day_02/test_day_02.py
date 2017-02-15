import pytest
from day_02 import translate_to_morse, morse_table

def test_translate_to_morse():
    assert translate_to_morse('a') == morse_table.get('a') + '___'