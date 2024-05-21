# Execute o seguinte comando no terminal
#  python -m unittest -v test/test_Q02.py
import unittest
import re
from parameterized import parameterized
from src.Q05 import pat02

class Test_Q05 (unittest.TestCase):
    @parameterized.expand([
        ['00','abcd@aaa.xxx.ra',True],
        ['01','g@d.daf.df', True],
        ['02','f4@356.ghj.ds',True],
        ['03','a_@d6g.dsf.df',True],
        ['04','a_77@5.das.hf',True],
        ['05','daagafa5656@f3f.das.fs',True],
        ['06','fas35___@ghhdhght.fgd.ht',True],
        ['07','6@aaa.xxx.ra',False],
        ['08','_@aaa.xxx.ra',False],
        ['09','@aaa.xxx.ra',False],
        ['10','a@a_.xxx.ra',False],
        ['11','a@_.xxx.ra',False],
        ['12','a@.xxx.ra',False],
        ['13','a@a.xx.ra',False],
        ['14','a@a.xxx.r',False],
        ['15','a@a.x4x.ra',False],
        ['16','a@a.xx_.ra',False],
        ['17','a@a.xxx.r6',False],
        ['18','',False]
    ])
    def test_base (self, name, str, expected_result):
        result = re.fullmatch(pat02,str)
        self.assertEqual(result is not None,expected_result)

    def test_instance (self):
        self.assertTrue('.' in pat02)
        self.assertTrue('_' in pat02)
        self.assertTrue(pat02 is not None)
        self.assertTrue(len(pat02) > 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
