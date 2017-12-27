#Python 2.7
pyg = 'ay'

original = raw_input('Enter a word: ').lower()
word = original.lower()
first = word[0]
if original.isalpha():
    if len(original) > 0:
        new_word = original + first + pyg
        new_word = new_word[1:len(new_word)]
        print(new_word)
    else:
        print 'empty'
else:
    print('Empty')
