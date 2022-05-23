import string

def ReadFile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read() # return a string


def CountChar(txt:str):
    upper, lower, digit, space, other = 0, 0, 0, 0, 0
    for ch in txt:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
        elif ch.isnumeric():
            digit = digit + 1
        elif ch.isspace():
            space = space + 1
        else:
            other = other + 1
    return upper, lower, digit, space, other


def ReplaceWithSpace(txt:str):
    ign = r'（!"#$%&()*+,./:;<=>?@[\]^_‘{|}~\）'
    for ch in ign:
        txt.replace(ch, ' ')
    return txt.split()


def CountWord(txt):
    return len(txt)


def CalcOffset(s:str):
    sum = 0
    for ch in s:
        sum = sum + ord(ch)
    return sum % 26


def Kaisi(txt:str, number:int):
    lower, upper = string.ascii_lowercase, string.ascii_uppercase
    before = lower + upper
    after = lower[number:] + lower[:number] + upper[number:] + upper[:number]
    table = ''.maketrans(before, after)
    return txt.translate(table)


if __name__ == '__main__':
    filename = 'mayun.txt'
    text = ReadFile(filename)
    wordsConnts = CountWord(ReplaceWithSpace(text))
    secret = input()
    offsetNumber = CalcOffset(secret)
    print(*CountChar(text))
    print(f'共有{wordsConnts + 1}单词')
    print(offsetNumber)
    print(Kaisi(text, offsetNumber))
