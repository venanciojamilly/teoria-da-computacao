# Execute o seguinte comando no terminal
#  python -m unittest -v test/test_Q02.py
import unittest
import re
from parameterized import parameterized
from src.Q02 import pat01

class Test_Q02 (unittest.TestCase):
    @parameterized.expand([
        ['00','/# abc #/',True],
        ['01','/##/', True],
        ['02','/#ry#/',True],
        ['03','/#    #/',True],
        ['04','/#f  n33532 #/',True],
        ['05','/#   k34#/',True],
        ['06','/#123456#/',True],
        ['07','#/   o#/',False],
        ['08','/#  uvxz#/  df#/',False],
        ['09','/#adds#/#',False],
        ['10','/#   dfdx 76#/  ',False],
        ['11','/#  ao56# #/',False],
        ['12','/# sfgfb64 lll/#',False],
        ['13','/# nnn nn/# fd #/',False],
        ['14','7a/#nn  #/',False],
        ['15','',False]
    ])
    def test_base (self, name, str, expected_result):
        result = re.fullmatch(pat01,str)
        self.assertEqual(result is not None,expected_result)

    def test_instance (self):
        self.assertTrue('#' in pat01)
        self.assertTrue('/' in pat01)
        self.assertTrue(pat01 is not None)
        self.assertTrue(len(pat01) > 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
