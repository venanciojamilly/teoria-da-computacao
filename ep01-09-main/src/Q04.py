from automata.fa.nfa import NFA

nfa02 = NFA(
        states={'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10'}, 
        input_symbols={'L', 'N', 'S', '@', 'P'}, 
        transitions={
            'q0': {'L': {'q1'}},
            'q1': {'L': {'q1'}, 'N': {'q1'}, 'S': {'q1'}, '@': {'q2'}},
            'q2': {'L': {'q3'}, 'N': {'q3'}},
            'q3': {'L': {'q3'}, 'N': {'q3'}, 'P': {'q4'}},
            'q4': {'L': {'q5'}},
            'q5': {'L': {'q6'}},
            'q6': {'L': {'q7'}},
            'q7': {'P': {'q8'}},
            'q8': {'L': {'q9'}},
            'q9': {'L': {'q10'}}
        }, 
        initial_state='q0', 
        final_states={'q10'}
)
