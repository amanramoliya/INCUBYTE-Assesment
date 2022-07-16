import string_calculator as calc
import pytest

def test_empty_string():
    assert calc.string_Calculator('') == 0

def test_single_number_string():
    assert calc.string_Calculator('6') == 6
    assert calc.string_Calculator('0') == 0
          
def test_two_numbers_string():
    assert calc.string_Calculator('1,4') == 5
    assert calc.string_Calculator('21,21') == 42

def test_multiple_numbers_string():
    assert calc.string_Calculator('1,2,3') == 6
    assert calc.string_Calculator('100,200,300,50,10,40') == 700

def test_new_line_between_numbers_string():
    assert calc.string_Calculator('1\n2,3') == 6
    assert calc.string_Calculator('10\n20\n20\n10,20\n20') == 100

def test_different_delimiter():
    assert calc.string_Calculator('//;\n1;2') == 3
    assert calc.string_Calculator('//;\n1;2;7\n10') == 20

def test_ignore_larger_than_1000():
    assert calc.string_Calculator('1000,100') == 100
    assert calc.string_Calculator('1\n2,3000') == 3
    assert calc.string_Calculator('//+\n1+2+7\n980') == 990

def test_any_length_delimiter():
    assert calc.string_Calculator('//***\n10***20***70\n1000') == 100
    assert calc.string_Calculator('//++\n1++2++7\n10') == 20

def test_multiple_delimiters():
    assert calc.string_Calculator('//+*\n1+2*7') == 10
    assert calc.add('//+%\n1+2%7\n10') == 20

def test_handle_negative_numbers():
    with pytest.raises(Exception,match = r'negatives not allowed[-3, -4]'):
        assert calc.add('-3,-4,3')
    
def test_any_length_multiple_delimiters():
    assert calc.add('//++%%\n1++2%%3') == 6
    assert calc.add('//++%\n1++2%7\n10') == 20


