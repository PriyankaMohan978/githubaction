import pytest

from add import add, sub, mul, div

def test_add():
    # compare actual output and excpected output

  assert add(2,3)== 5

  def test_sub():
    # compare actual output and excpected output

   assert sub(5,3)== 2

   def test_mul():
    # compare actual output and excpected output

    assert mul(2,3)== 6

    def test_div():
    # compare actual output and excpected output

     assert add(2,2)== 1