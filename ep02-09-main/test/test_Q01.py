# Execute o seguinte comando no terminal
#  python -m unittest -v test/test_Q01.py
import unittest
from automata.tm.dtm import DTM
from parameterized import parameterized
from util.util import dtm_configurations
from src.Q01 import dtm1

class Test_Q01 (unittest.TestCase):
    @parameterized.expand([
        ['00','ab','ab'],
        ['01','AB','ab'],
        ['02','',''],
        ['03','B','b'],
        ['04','A','a'],
        ['05','aAb','aab'],
        ['06','bBA','bba'],
        ['07','aaaaaa','aaaaaa'],
        ['08','aaaBaaa','aaabaaa'],
        ['09','AAABaaa','aaabaaa'],
        ['10','babababa','babababa'],
        ['11','BBBBBAb','bbbbbab']
    ])
    def test_base (self, name, str, expected_output):
        gen = dtm1.read_input_stepwise(str)
        state,output,_ = dtm_configurations(gen)
        self.assertEqual(output.strip(dtm1.blank_symbol),expected_output)
        self.assertTrue(state in dtm1.final_states)

    def test_instance (self):
        self.assertTrue(isinstance(dtm1,DTM))
        self.assertSetEqual(dtm1.input_symbols,{'a','b','A','B'})
        self.assertEqual(dtm1.blank_symbol,'.')

if __name__ == '__main__':
    unittest.main(verbosity=2)