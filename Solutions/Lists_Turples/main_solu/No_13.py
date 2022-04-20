def format_sort_records(turples):
    for i in turples:
        print(i[1].ljust(10, ' '), i[0].ljust(10, ' ') + '%5.2f'%(i[-1]))

format_sort_records([('Donald', 'Trump', 7.85),
                    ('Vladimir', 'Putin', 3.626),
                    ('Jinping', 'Xi', 10.603)])
