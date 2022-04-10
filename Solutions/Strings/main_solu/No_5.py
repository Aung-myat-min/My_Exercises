def translation_to_Paglatin(string):
    string = string.lower()
    if string[0] in list('aeiou'):
        return string + 'way'
    else:
        re_str = string[1:]
        return re_str + string[0] + 'ay'

print(translation_to_Paglatin('eat'))
print(translation_to_Paglatin('stay'))