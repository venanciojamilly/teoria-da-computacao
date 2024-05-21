# Execute o seguinte comando no terminal
#  python -m unittest -v test/test_Q03.py
import unittest
from automata.tm.mntm import MNTM
from parameterized import parameterized
from src.Q03 import mntm3

class Test_Q03 (unittest.TestCase):
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
        gen = mntm3.read_input_stepwise(str)
        output_conf = list(list(gen)[-1])
        state = output_conf[0].state
        output = "".join(output_conf[0].tapes[1].tape)
        self.assertEqual(output.strip(mntm3.blank_symbol),expected_output)
        self.assertTrue(state in mntm3.final_states)

    def test_instance (self):
        self.assertTrue(isinstance(mntm3,MNTM))
        self.assertSetEqual(mntm3.input_symbols,{'a','b','+'})
        self.assertEqual(mntm3.blank_symbol,'.')

if __name__ == '__main__':
    unittest.main(verbosity=2)