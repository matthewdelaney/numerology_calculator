translations = [['a', 'j', 's'],
                ['b', 'k', 't'],
                ['c', 'l', 'u'],
                ['d', 'm', 'v'],
                ['e', 'n', 'w'],
                ['f', 'o', 'x'],
                ['g', 'p', 'y'],
                ['h', 'q', 'z'],
                ['i', 'r']]

lookup_table = {}

for i, t in enumerate(translations):
    lookup_table.update(dict.fromkeys(t, i+1))


def translate(text):
    translation = ''
    for c in text.lower():
        if c != ' ':
            translation += str(lookup_table[c])

    return translation


def name_sum(digits):
     digit_sum = 0
     for d in digits:
             digit_sum += int(d)
     if len(str(digit_sum)) == 1:
             return digit_sum
     else:
             return name_sum(str(digit_sum))


if __name__ == '__main__':
    name = input('Name: ')
    print(name_sum(translate(name)))
