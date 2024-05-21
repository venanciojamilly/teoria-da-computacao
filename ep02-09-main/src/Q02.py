from automata.tm.dtm import DTM

dtm2 = DTM(
    states={'start', 'backToStart', 'track','trackA','trackB','final','done'},
    input_symbols={'a', 'b','+'},
    tape_symbols={'a', 'b', '+', '.'},
    transitions={
        'start' : {
            'a': ('start', 'a', 'R'),
            'b': ('start', 'b', 'R'),
            '+': ('track', '+', 'N'),
            '.': ('done', '.', 'N')
        },
        
        'track':{
            'a': ('trackA', '+', 'L'),
            'b': ('trackB', '+', 'L'),
            '+': ('track', '+', 'R'),
            '.': ('final', '.', 'L'),
        },
        
        'trackA':{
            '+': ('backToStart', 'a', 'N'),
        },
        
        'trackB':{
            '+': ('backToStart', 'b', 'N'),
        },
        
        'backToStart':{
            'a': ('backToStart', 'a', 'L'),
            'b': ('backToStart', 'b', 'L'),
            '+': ('track', '+', 'N'),
            '.': ('start', '.', 'R'),
        },
        
        'final' : {
            'a': ('final', 'a', 'L'),
            'b': ('final', 'b', 'L'),
            '+': ('final', '.', 'L'),
            '.': ('done', '.', 'N')
        },
        
    },
    initial_state='start',
    blank_symbol='.',
    final_states={'done'}
)