from Functions.getdaydate import getdaydate
from datetime import date
import pytest

def test_occurances():
    assert getdaydate('First','Monday',1,2020) == date(2020, 1, 6)
    assert getdaydate('Second','Tuesday',2,2020) == date(2020, 2, 11)
    assert getdaydate('Third','Friday',3,2020) == date(2020, 3, 20)
    assert getdaydate('Fourth','Sunday',4,2020) == date(2020, 4, 26)
    assert getdaydate('Last','Wednesday',6,2020) == date(2020, 6, 24)

def test_weeks():
    assert getdaydate('First','Monday',12,2021) == date(2021, 12, 6)
    assert getdaydate('Second','Tuesday',11,2020) == date(2020, 11, 10)
    assert getdaydate('Last','Wednesday',8,2020) == date(2020, 8, 26)
    assert getdaydate('Third','Thursday',10,2020) == date(2020, 10, 15)
    assert getdaydate('Third','Friday',9,2020) == date(2020, 9, 18)
    assert getdaydate('Fourth','Sunday',8,2020) == date(2020, 8, 23)
    assert getdaydate('Last','Wednesday',7,2020) == date(2020, 7, 29)

def test_Failures():
    with pytest.raises(ValueError) as exc_info:
        assert getdaydate('x','Wednesday',7,2020)
    assert str(exc_info.value)  == "Error: x is not in ('First', 'Second', 'Third', 'Fourth', 'Last')"
    with pytest.raises(ValueError) as exc_info:
        assert getdaydate('Second','Wed',7,2020)
    assert str(exc_info.value)  == "Error: Wed is not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')"
    with pytest.raises(ValueError) as exc_info:
        assert getdaydate('Second','Wednesday',0,2020)
    assert str(exc_info.value)  == "Error: 0 is not in range (1 - 12)"
    with pytest.raises(ValueError) as exc_info:
        assert getdaydate('Second','Wednesday',12,20200)
    assert str(exc_info.value)  == "Error: 20200 is not in range  (1000 - 9999)"

"""
python -m pipenv run pytest
python -m pipenv shell
py.test -v 
"""