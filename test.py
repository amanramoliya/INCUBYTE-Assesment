import StringCalculator as calc
import pytest

def test_empty_string():
    assert calc.string_Calculator('') == 0

def test_single_number_string():
    assert calc.string_Calculator('6') == 6
    assert calc.string_Calculator('0') == 0
          
def test_two_numbers_string():
    assert calc.string_Calculator('1,4') == 1
    assert calc.string_Calculator('21,21') == 21

def test_odd_position_numbers():
    assert calc.string_Calculator('1,3,2') == 3

def test_multiple_numbers_string():
    assert calc.string_Calculator('1,2,3') == 4
    assert calc.string_Calculator('100,200,300,50,10,40') == 410

def test_new_line_between_numbers_string():
    assert calc.string_Calculator('1\n2,3') == 4
    assert calc.string_Calculator('10\n20\n20\n10,20\n20') == 50

def test_different_delimiter():
    assert calc.string_Calculator('//;\n1;2') == 1
    assert calc.string_Calculator('//;\n1;2;7\n10') == 8

def test_ignore_larger_than_1000():
    assert calc.string_Calculator('1000,100') == 0
    assert calc.string_Calculator('1\n2,3000') == 1
    assert calc.string_Calculator('//+\n1+2+7\n980') == 8

def test_any_length_delimiter():
    assert calc.string_Calculator('//***\n10***20***70\n1000') == 80
    assert calc.string_Calculator('//++\n1++2++7\n10') == 8

def test_multiple_delimiters():
    assert calc.string_Calculator('//+*\n1+2*7') == 8
    assert calc.string_Calculator('//+%\n1+2%7\n10') == 8

def test_handle_negative_numbers():
    with pytest.raises(Exception,match = r'negatives not allowed[-3, -4]'):
        assert calc.string_Calculator('-3,-4,3')
    
def test_any_length_multiple_delimiters():
    assert calc.string_Calculator('//++%%\n1++2%%3') == 4
    assert calc.string_Calculator('//++%\n1++2%7\n10') == 8


