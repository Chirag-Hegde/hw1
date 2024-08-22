import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from myfile_Melika import hello, age, count, sqaure

def test_hello():
    assert hello('Melika') == 'Hello Dear Melika'

def test_age():
    assert age(2000, 2024) == 24

def test_count():
    assert count(6) == 15

def test_square():
    assert sqaure(10) == 100