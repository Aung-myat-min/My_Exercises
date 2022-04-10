def translation_to_Paglatin(string):
    strings = string.lower()
    punc = ''
    string = ''
    if strings[-1] in list('.,:;?!'):
        string = strings.replace(strings[-1], '')
        punc = strings[-1]
    else:
        string = strings
    if string[0] in list('aeiou'):
        a = string + 'way' + punc
        return a.title()
    else:
        re_str = string[1:]
        a = re_str + string[0] + 'ay' + punc
        return a.title()

print(translation_to_Paglatin('eat!'))
print(translation_to_Paglatin('stay'))

def more_vowel(string):
    string = string.lower()
    if string[0] in list('aeiou'):
        return string + 'way'
    else:
        num_vow = 0
        for i in string:
            if i in list('aeiou'):
                num_vow += 1
        if num_vow > 0:
            return string + 'way'
        else:
            return string[1:] + string[0] + 'ay'

print(more_vowel('wind'))