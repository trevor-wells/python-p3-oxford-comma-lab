def oxford_comma(items):
    if len(items) == 2 or len(items) == 1:
        return ' and '.join(items)
    last = items[-1]
    joined = ', '.join(items)
    getting_there = joined.split(f'{last}')
    almost = 'and '.join(getting_there)
    return almost + last
