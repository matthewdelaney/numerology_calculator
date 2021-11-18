lookup_table = {'a':1, 'j':1, 's':1,
                'b':2, 'k':2, 't':2,
                'c':3, 'l':3, 'u':3,
                'd':4, 'm':4, 'v':4,
                'e':5, 'n':5, 'w':5,
                'f':6, 'o':6, 'x':6,
                'g':7, 'p':7, 'y':7,
                'h':8, 'q':8, 'z':8,
                'i':9, 'r':9}

def translate(text):
    translation = ''
    for c in text.lower():
        if c != ' ':
            translation += str(lookup_table[c])

    return translation


def nsum(digits):
     digit_sum = 0
     for d in digits:
             digit_sum += int(d)
     if len(str(digit_sum)) == 1:
             return digit_sum
     else:
             return nsum(str(digit_sum))

if __name__ == '__main__':
    name = input('Name: ')
    print(nsum(translate(name)))