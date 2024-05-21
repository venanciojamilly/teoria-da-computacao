from automata.fa.dfa import DFA


dfa01 = DFA(
        states={'q0','q1','q2', 'q3', 'q4', 'qe'},
        input_symbols={'l', 'n', 'b', '/', '#'},
        transitions={
            'q0': {'l': 'qe', 'n': 'qe', 'b': 'qe', '#': 'qe', '/': 'q1'},
            'q1': {'l': 'qe', 'n': 'qe', 'b': 'qe', '#': 'q2', '/': 'q1'},
            'q2': {'l': 'q2', 'n': 'q2', 'b': 'q2', '#': 'q3', '/': 'qe'},
            'q3': {'l': 'qe', 'n': 'qe', 'b': 'qe', '#': 'qe', '/': 'q4'},
            'q4': {'l': 'qe', 'n': 'qe', 'b': 'qe', '#': 'qe', '/': 'qe'},
            'qe': {'l': 'qe', 'n': 'qe', 'b': 'qe', '#': 'qe', '/': 'qe'},
        },
        initial_state= 'q0',
        final_states={'q4'}
)
