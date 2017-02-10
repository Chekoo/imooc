def f(sentece):
    vChar, vowel, word, consonant = 'aeiou', 0, 0, 0
    for eChar in sentence:
        if eChar.isalpha():
            if eChar in vChar:
                vowel += 1
            else:
                consonant += 1

    return (vowel, consonant, len([eWord for eWord in sentece.split()]))


sentence = raw_input('Input a sentence...\n')
print 'vowel：%d, consonant: %d, word:%d' % f(sentence)