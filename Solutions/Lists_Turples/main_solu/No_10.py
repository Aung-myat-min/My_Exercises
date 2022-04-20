def adding_anything(*anything):
    if not anything:
        return 'empty item'
    returning = anything[0]
    for i in anything[1:]:
        returning += i
    return returning

print(adding_anything('a', 'u', 'n', 'g'))
