class morse():

    morseVals = {'a' : '.-', 'b' : '-...', 'c' : '-.-.',
                'd' : '-..', 'e' : '.', 'f' : '..-.',
                'g' : '--.', 'h' : '....', 'i' : '..',
                'j' : '.---', 'k' : '-.-', 'l' : '.-..',
                'm' : '--', 'n' : '-.', 'o' : '---',
                'p' : '.--.', 'q' : '--.', 'r' : '.-.',
                's' : '...', 't' : '-', 'u' : '..-',
                'v' : '...-', 'w' : '.--', 'x' : '-..-',
                'y' : '-.--', 'z' : '--..', ' ' : '  '}
    input = raw_input('Enter String: ')
    input = input.lower()
    input.split()
    t = []
    for i in input:
        #if (i in morseVals):
        t.append(morseVals.get(i))

    #print(morseVals.get('R'))
    display = ''.join(t)
    print(display)

morse()
