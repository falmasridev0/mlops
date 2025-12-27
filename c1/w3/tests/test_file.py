import pytest
def test_function():
    assert 10 == 10

class TestClass:
    def test_method(self):
        assert 10 + 5 == 15

    @pytest.mark.parametrize("a, b",[(1,3),[5,2]])
    def test_sum(self,a,b):
        c = 10
        a = -1
        assert a + b == a+b

