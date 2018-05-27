#basic code structure of project from...
#https://github.com/morphatic/isat252u18examples/blob/master/python/converter/test_converter.py
#and
#https://github.com/morphatic/isat252u18examples/blob/master/python/lms/test_student.py

# import pytest for using utilities
from pytest import approx 

# import the code to be tested
from pythonian import kpm, mpk, gpl, lpg, mpg, kpl

# write a smoke test
def test_smoke():
  assert True == True

# test conversion from miles to kilometers
def test_kpm():
  assert kpm(0) == 0
  assert kpm(1) == approx(1.6093)
  assert kpm(50) == approx(80.465)
  assert kpm(100) == approx(160.93)
  assert kpm(150) == approx(241.395)

# test conversion from kilometers to miles
def test_mpk():
  assert mpk(0) == 0
  assert mpk(1) == approx(0.621388)
  assert mpk(50) == approx(31.0694)
  assert mpk(100) == approx(62.1388)
  assert mpk(150) == approx(93.2082)

# test conversion from gallons to litters
def test_gpl():
  assert gpl(0) == 0
  assert gpl(1) == approx(3.78541)
  assert gpl(50) == approx(189.2706267)
  assert gpl(100) == approx(378.5412534)
  assert gpl(150) == approx(567.8118801)

# test conversion from litters to gallons
def test_lpg():
  assert lpg(0) == 0
  assert lpg(1) == approx(0.264172)
  assert lpg(50) == approx(13.2086)
  assert lpg(100) == approx(26.4172)
  assert lpg(150) == approx(39.6258)

def test_mpg():
  assert mpg(0) == 0
  assert mpg(1) == approx(2.35221061)
  assert mpg(50) == approx(117.610530487)
  assert mpg(100) == approx(235.221060974)
  assert mpg(150) == approx(352.831591461)

def test_kpl():
  assert kpl(0) == 0
  assert kpl(1) == approx(0.425132)
  assert kpl(50) == approx(21.25659998)
  assert kpl(100) == approx(42.51319996)
  assert kpl(150) == approx(63.76979994)

#^^^EVERYTHING HERE UP IS GOOD!^^^

from pythonian import car

#from: https://programmingideaswithjake.wordpress.com/2016/05/07/object-literals-in-python/
class Object:
  def __init__(self, **attributes):
    self.__dict__.update(attributes)

#from Morgan Benton code example (email)
corolla = car(mpg = 32)

def test_corolla_has_kpl():
  assert hasattr(corolla, "kilometers_per_litter")
  assert corolla.kilometers_per_litter == approx(32 * 1.6093 * 0.264172, abs = 0.001)

corolla = car(kpl = 13.604224)

def test_corolla_has_mpg():
  assert hasattr(corolla, "miles_per_gallon")
  assert corolla.miles_per_gallon == approx(13.604224 / 1.6093 / 0.264172, abs = 0.001)

 