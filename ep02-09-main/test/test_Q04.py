# Execute o seguinte comando no terminal
#  python -m unittest -v test/test_Q04.py
import unittest
from automata.tm.mntm import MNTM
from automata.base.exceptions import RejectionException
from parameterized import parameterized
from src.Q04 import mntm4

class Test_Q04 (unittest.TestCase):
    @parameterized.expand([
        ['00','#a', True],
        ['01','#b', True],
        ['02','#ab', True],
        ['03','#bbbbbb', True],
        ['04','a#abaaaa', True],
        ['05','b#abbabbaba',True],
        ['06','a#ababa', True],
        ['07','a#bbbbabbb', True],
        ['08','a#bbbba',True],
        ['09','abab#abaaaaaabab',True],
        ['10','aaa#abaaaaaabab',True],
        ['11','aaaaa#abaaaaaabab',True],
        ['12','aba#abbabaaaaabab',True],
        ['13','aba#abaaaaaabab',True],
        ['14','aba#aaaaaaaaba',True],
        ['15','#',True],
        ['16','aaaa#aaaaaa',True],
        ['17','bb#bbbbb',True],
        ['18','b#b',True],
        ['19','a#a',True],
        ['20','aa#aab',True],
        ['21','aa#baa',True],
    ])
    def test_base_accept (self, name, str, expected_output):
        gen = mntm4.read_input_stepwise(str)
        output_conf = list(list(gen)[-1])
        state = output_conf[0].state
        self.assertTrue(state in mntm4.final_states)

    @parameterized.expand([
        ['00','abab#abaaaaaabb',False],
        ['01','bbb#abaaaaaabab',False],
        ['02','bbbbb#abaaaaaabab',False],
        ['03','aba#', False],
        ['04','a#bbbbb', False],
        ['05', 'ab#ba', False],
        ['06', 'aba', False],
        ['07', 'aaa#a', False]
    ])
    def test_base_reject (self, name, str, expected_output):
        gen = mntm4.read_input_stepwise(str)
        with self.assertRaises(RejectionException):
           lista = [c for c in gen]
     

    def test_instance (self):
        self.assertTrue(isinstance(mntm4,MNTM))
        self.assertSetEqual(mntm4.input_symbols,{'a','b','#'})
        self.assertEqual(mntm4.blank_symbol,'.')

if __name__ == '__main__':
    unittest.main(verbosity=2)