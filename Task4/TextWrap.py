def wrap(string, max_width):
    '''Wraps the string into a paragraph of width w'''
    string = [c for c in string]

    for i in range(max_width, len(string) + max_width, max_width+1):
        string.insert(i, '\n')
    return ("").join(string)