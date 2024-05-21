from automata.tm.mntm import MNTM

mntm3 = MNTM(
    states={'start', 'done'},
    input_symbols={'a', 'b', '+'},
    tape_symbols={'a', 'b', '+', '.'},
    n_tapes=2,
    transitions={
      'start': {
            ('a', '.'): [('start', (('a', 'R'), ('a', 'R')))],
            ('b', '.'): [('start', (('b', 'R'), ('b', 'R')))],
            ('+', '.'): [('start', (('+', 'R'), ('.', 'N')))],
            ('.', '.'): [('done', (('.', 'N'), ('.', 'N')))]
        },
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'},
)

  