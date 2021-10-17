def mutate_string(string, position, character):
    """a=list(string)
    a.insert(position,character)
    listToStr = ''.join([str(elem) for elem in a])
    return listToStr"""
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)