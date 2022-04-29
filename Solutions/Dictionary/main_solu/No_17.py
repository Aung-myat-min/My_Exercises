def how_many_different_numbers(lists):
    return f'In the length of a {len(lists)} list, it contains {len(set(lists))} numbers'

print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))