# Execute o seguinte comando no terminal
#  python -m unittest -v test/test_Q03.py
import unittest
from automata.fa.nfa import NFA
from parameterized import parameterized
from src.Q03 import nfa01

class Test_Q03 (unittest.TestCase):
    @parameterized.expand([
        ['00','21B',True],
        ['01','111S', True],
        ['02','12P',True],
        ['03','1S2P',True],
        ['04','SBP111S',True],
        ['05','1S1S1S',True],
        ['06','21S',True],
        ['07','21',False],
        ['08','111',False],
        ['09','12',False],
        ['10','22B',False],
        ['11','121E',False],
        ['12','2S',False],
        ['13','2',False],
        ['14','BB',False],
        ['15','S',False],
        ['16','11BB',False],
        ['17','111B1',False],
        ['18','11P1',False],
        ['19','',False]
    ])

    def test_base (self, name, str, expected_result):
        result = nfa01.accepts_input(str)
        self.assertEqual(result, expected_result)

    def test_instance (self):
        self.assertTrue(isinstance(nfa01,NFA))
        self.assertSetEqual(nfa01.input_symbols,{'1','2','B','S','P'})

if __name__ == '__main__':
    unittest.main(verbosity=2)