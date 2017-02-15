#
# This program translates input text to morse code
#

morse_table = {'a': '· −',
               'b': '− · · ·',
               'c': '− · − ·',
               'd': '− · ·',
               'e': '·',
               'f': '· · − ·',
               'g': '− − ·',
               'h': '· · · ·',
               'i': '· ·',
               'j': '· − − −',
               'k': '− · −',
               'l': '· − · ·',
               'm': '− −',
               'n': '− ·',
               'o': '− − −',
               'p': '· − − ·',
               'q': '− − · −',
               'r': '· − ·',
               's': '· · ·',
               't': '−',
               'u': '· · −',
               'v': '· · · −',
               'w': '· − −',
               'x': '− · · −',
               'y': '− · − −',
               'z': '− − · ·',
               '1': '· − − − −',
               '2': '· · − − −',
               '3': '· · · − −',
               '4': '· · · · −',
               '5': '· · · · ·',
               '6': '− · · · ·',
               '7': '− − · · ·',
               '8': '− − − · ·',
               '9': '− − − − ·',
               '0': '− − − − −',
               ' ': '   '}


def translate_to_morse(input_text):
    _translation = []
    for symbol in input_text:
        morse_symbol = morse_table.get(symbol.lower())
        _translation.append(morse_symbol)
        _translation.append('___')
    return ''.join(_translation)


if __name__ == '__main__':
    input_text = input('Enter text to translate into morse code: ')
    print(input_text)
    morse = translate_to_morse(input_text)
    print('Your translation: {}'.format(morse))
