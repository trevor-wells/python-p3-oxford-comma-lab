def oxford_comma(items):
    if len(items) == 2 or len(items) == 1:
        return ' and '.join(items)
    last = items[-1]
    joined = ', '.join(items)
    getting_there = joined.split(f'{last}')
    almost = 'and '.join(getting_there)
    return almost + last

#wow this is so much more elegant than mine
def oxford_comma(items):
    if len(items) > 1:
        items[-1] = "and " + items[-1]

    if len(items) > 2:
        return ', '.join(items)
    else:
        return ' '.join(items)
