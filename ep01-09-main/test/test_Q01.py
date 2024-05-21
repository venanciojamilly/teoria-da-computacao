# Execute o seguinte comando no terminal
#  python -m unittest -v test/test_Q01.py
import unittest
from automata.fa.dfa import DFA
from parameterized import parameterized
from src.Q01 import dfa01

class Test_Q01 (unittest.TestCase):
    @parameterized.expand([
        ['00','/#blllb#/',True],
        ['01','/##/', True],
        ['02','/#ll#/',True],
        ['03','/#bbbb#/',True],
        ['04','/#lbblnlllb#/',True],
        ['05','/#bbblnn#/',True],
        ['06','/#nnnnnn#/',True],
        ['07','#/bbbl#/',False],
        ['08','/#bbllllnn#/bbbll#/',False],
        ['09','/#llll#/#',False],
        ['10','/#bbblllbnn#/bb',False],
        ['11','/#bbllnn#b#/',False],
        ['12','/#bllllbnnblll/#',False],
        ['13','/#bnnnbnn/#nnn#/',False],
        ['14','nl/#nnbb#/',False],
        ['15','',False]
    ])

    def test_base (self, name, str, expected_result):
        result = dfa01.accepts_input(str)
        self.assertEqual(result, expected_result)

    def test_instance (self):
        self.assertTrue(isinstance(dfa01,DFA))
        self.assertSetEqual(dfa01.input_symbols,{'l','n','b','/','#'})

if __name__ == '__main__':
    unittest.main(verbosity=2)