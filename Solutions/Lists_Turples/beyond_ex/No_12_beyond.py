def most_repeating_vowel(words):
    returning = ''
    g = {}
    for i in words:
        di = {}
        chars = []
        for j in i:
            if j in list('aeiou'):
                if not j in chars:
                    di[j] = i.count(j)
                    chars.append(j)
        g[i] = max(di.values())
    new_dict = dict([(k,v) for v,k in g.items()])
    returning = new_dict.get(max(new_dict.keys()))
    return returning

print(most_repeating_vowel(['this', 'is', 'an', 'elementary', 'test', 'example', 'aeaaaaaaaaa']))