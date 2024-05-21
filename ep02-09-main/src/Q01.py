from automata.tm.dtm import DTM

dtm1 = DTM(
    states={'start', 'done'},
    input_symbols={'a', 'b', 'A', 'B'},
    tape_symbols={'a', 'b', 'B', 'A', '.'},
    transitions={
        'start': {
            'a': ('start', 'a', 'R'),
            'b': ('start', 'b', 'R'),
            'A': ('start', 'a', 'R'),
            'B': ('start', 'b', 'R'),
            '.': ('done', '.', 'R')
        }
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'}
)
    
