# Execute o seguinte comando no terminal
#  python -m unittest -v test/test_Q02.py
import unittest
from automata.tm.dtm import DTM
from parameterized import parameterized
from util.util import dtm_configurations
from src.Q02 import dtm2

class Test_Q02 (unittest.TestCase):
    @parameterized.expand([
        ['00','ab','ab'],
        ['01','a+baa+a','abaaa'],
        ['02','',''],
        ['03','b','b'],
        ['04','a','a'],
        ['05','a+b','ab'],
        ['06','b+a','ba'],
        ['07','aa++aaa','aaaaa'],
        ['08','+a+a','aa'],
        ['09','+',''],
        ['10','++',''],
        ['11','+aa+','aa'],
        ['12','+a+b+','ab'],
        ['13','aaa+a+b+bbb+aa','aaaabbbbaa'],
        ['14','b+++b+a','bba'],
        ['15','b+++b++a','bba'],
        ['16','b+++','b'],
        ['17','a+a+b++bb+++','aabbb'],
        ['18','aaaababaabaabaa+a+abbbbbbba','aaaababaabaabaaaabbbbbbba'],
        ['19','aaaaaabaaaaaaaaaaaaa','aaaaaabaaaaaaaaaaaaa'],
        ['20','bbbbbbb','bbbbbbb'],
    ])

    def test_base (self, name, str, expected_output):
        gen = dtm2.read_input_stepwise(str)
        state,output,_ = dtm_configurations(gen)
        self.assertEqual(output.strip(dtm2.blank_symbol),expected_output)
        self.assertTrue(state in dtm2.final_states)

    def test_instance (self):
        self.assertTrue(isinstance(dtm2,DTM))
        self.assertSetEqual(dtm2.input_symbols,{'a','b','+'})
        self.assertEqual(dtm2.blank_symbol,'.')

if __name__ == '__main__':
    unittest.main(verbosity=2)
