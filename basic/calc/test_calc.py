import pytest
import calc

@pytest.mark.parametrize(
    ["test_input", "expectedadd","expectedsub"] ,[([10, 5],15,5),([3, 10],13,-7)]
)

#この関数にはparametrizeで定義した数を全て渡す
def test_calcadd(test_input, expectedadd,expectedsub):
    assert calc.calcadd(*test_input) == expectedadd
    assert calc.calcsub(*test_input) == expectedsub
