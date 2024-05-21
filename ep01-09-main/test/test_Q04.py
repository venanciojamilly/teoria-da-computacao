# Execute o seguinte comando no terminal
#  python -m unittest -v test/test_Q04.py
import unittest
from automata.fa.nfa import NFA
from parameterized import parameterized
from src.Q04 import nfa02

class Test_Q04 (unittest.TestCase):
    @parameterized.expand([  # . é substituído por P na função de teste
        ['00','LLLL@LLL.LLL.LL',True],
        ['01','L@L.LLL.LL', True],
        ['02','LN@NNN.LLL.LL',True],
        ['03','LS@LN.LLL.LL',True],
        ['04','LSNN@N.LLL.LL',True],
        ['05','LLLLLLLNNN@LNL.LLL.LL',True],
        ['06','LLLNSSS@LLLLLLLLL.LLL.LL',True],
        ['07','N@LLL.LLL.LL',False],
        ['08','S@LLL.LLL.LL',False],
        ['09','@LLL.LLL.LL',False],
        ['10','L@LS.LLL.LL',False],
        ['11','L@S.LLL.LL',False],
        ['12','L@.LLL.LL',False],
        ['13','L@L.LL.LL',False],
        ['14','L@L.LLL.L',False],
        ['15','L@L.LNL.LL',False],
        ['16','L@L.LLS.LL',False],
        ['17','L@L.LLL.NL',False],
        ['18','',False]
    ])

    def test_base (self, name, str, expected_result):
        result = nfa02.accepts_input(str.replace('.','P'))
        self.assertEqual(result, expected_result)

    def test_instance (self):
        self.assertTrue(isinstance(nfa02,NFA))
        self.assertSetEqual(nfa02.input_symbols,{'N', '@', 'S', 'L', 'P'})

if __name__ == '__main__':
    unittest.main(verbosity=2)