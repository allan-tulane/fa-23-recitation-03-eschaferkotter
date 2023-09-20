from main import *


## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2
  assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3
  assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10 * 10
  assert quadratic_multiply(BinaryNumber(100), BinaryNumber(100)) == 100 * 100
