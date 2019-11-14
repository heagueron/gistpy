# Simple assertions unit test
from cool_para import *


def test_cool_para():

    assert CoolPara('not enough words') == False, "Should be False"
    assert CoolPara('not enough words with rare letters gbgb nhnhnhn nhhjjmjm nhnhn nhnhn nhnhnh') == False, "Should be False"
    assert CoolPara('xthis qhave jenough words with rare xletters and_xqnhnhnhn long_nhhjjmjm words_nhnhn nhnhn nhnhnh') == True, "Should be True"

if __name__ == "__main__":
    test_cool_para()
    print("Everything passed")


        