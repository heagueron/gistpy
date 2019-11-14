import unittest
from cool_para import *

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 6")

class KoolPara(unittest.TestCase):

    p1 = 'not enough words'
    p2 = 'not enough words with rare letters gbgb nhnhnhn nhhjjmjm nhnhn nhnhn nhnhnh'
    p3 = 'xthis qhave jenough words with rare xletters and_xqnhnhnhn long_nhhjjmjm words_nhnhn nhnhn nhnhnh'

    def test_xmul(self):
        self.assertEqual(xmul(2,2,2), 6, "Should be 6")

    def test_words_qty(self):
        self.assertEqual(CoolPara('not enough words'), False, "Should be False")

    def test_words_len(self):
        self.assertEqual(CoolPara('not enough words with rare letters gbgb nhnhnhn nhhjjmjm nhnhn nhnhn nhnhnh'), False, "Should be False")

    def test_word_rare(self):
        self.assertEqual(CoolPara('xthis qhave jenough words with rare xletters and_xqnhnhnhn long_nhhjjmjm words_nhnhn nhnhn nhnhnh'), True, "Should be True")

if __name__ == '__main__':
    unittest.main()