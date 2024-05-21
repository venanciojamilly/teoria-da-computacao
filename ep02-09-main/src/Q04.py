from automata.tm.mntm import MNTM

mntm4 = MNTM(
    states={'start', 'foward', 'copy', 'back', 'backFirstLine', 'test', 'backAndErase', 'erase', 'done'},
    input_symbols={'a', 'b', '#'},
    tape_symbols={'a', 'b', '#', '.'},
    n_tapes=2,
    transitions={
      'start': {
            ('a', '.'): [('foward', (('a', 'R'), ('.', 'R')))],
            ('b', '.'): [('foward', (('b', 'R'), ('.', 'R')))],
            ('#', '.'): [('done', (('#', 'R'), ('.', 'R')))],
        },
      'foward': {
            ('a', '.'): [('foward', (('a', 'R'), ('.', 'R')))],
            ('b', '.'): [('foward', (('b', 'R'), ('.', 'R')))],
            ('#', '.'): [('copy', (('#', 'R'), ('#', 'R')))],
        },
      'copy': {
            ('a', '.'): [('copy', (('a', 'R'), ('a', 'R')))],
            ('b', '.'): [('copy', (('b', 'R'), ('b', 'R')))],
            ('.', '.'): [('back', (('.', 'L'), ('.', 'L')))],
        },
      'back': {
            ('a', 'a'): [('back', (('a', 'L'), ('a', 'L')))],
            ('b', 'b'): [('back', (('b', 'L'), ('b', 'L')))],
            ('#', '#'): [('backFirstLine', (('#', 'L'), ('#', 'N')))],
        },
      'backFirstLine': {
            ('a', '#'): [('backFirstLine', (('a', 'L'), ('#', 'N')))],
            ('b', '#'): [('backFirstLine', (('b', 'L'), ('#', 'N')))],
            ('.', '#'): [('test', (('.', 'R'), ('#', 'R')))],
        },
      'test': {
            ('a', 'a'): [('test', (('a', 'R'), ('a', 'R')))],
            ('a', 'b'): [('backAndErase', (('a', 'R'), ('b', 'R')))],
            ('b', 'a'): [('backAndErase', (('b', 'R'), ('a', 'R')))],
            ('b', 'b'): [('test', (('b', 'R'), ('b', 'R')))],
            ('#', 'a'): [('done', (('#', 'R'), ('a', 'R')))],
            ('#', 'b'): [('done', (('#', 'R'), ('b', 'R')))],
            ('#', '.'): [('done', (('#', 'R'), ('.', 'R')))],
        },
      'backAndErase': {
            ('a', 'a'): [('backAndErase', (('a', 'L'), ('a', 'L')))],
            ('a', 'b'): [('backAndErase', (('a', 'L'), ('b', 'L')))],
            ('b', 'a'): [('backAndErase', (('b', 'L'), ('a', 'L')))],
            ('b', 'b'): [('backAndErase', (('b', 'L'), ('b', 'L')))],
            ('.', '#'): [('erase', (('.', 'N'), ('#', 'R')))],
            ('#', 'a'): [('backAndErase', (('#', 'L'), ('a', 'L')))],
            ('#', 'b'): [('backAndErase', (('#', 'L'), ('b', 'L')))],
            ('#', '#'): [('backAndErase', (('#', 'L'), ('#', 'N')))],
        },
      'erase': {
            ('.', 'a'): [('test', (('.', 'R'), ('#', 'R')))],
            ('.', 'b'): [('test', (('.', 'R'), ('#', 'R')))],
        },
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'},
)

