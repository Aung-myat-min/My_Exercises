def pl_sentence(sentence):
    sentence = sentence.split()
    solu = ''
    for i in sentence:
        if i[0] in list('aeiou'):
            solu += i + 'way' + ' '
        else:
            solu += i[1:] + i[0] + 'ay' + ' '

    print(solu.strip())

pl_sentence('this is a test translation')
