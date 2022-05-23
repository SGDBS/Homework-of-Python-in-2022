ign = '（!"#$%&()*+,./:;<=>?@[\]^_‘{|}~\n）'

def ReadFile(filename):
    with open (filename) as file:
        text = file.readlines()
        text = ''.join(text)
        for ch in ign:
            text = text.replace(ch, ' ')
        print(len(text.split()))


if __name__ == '__main__':
    fileName = input()
    ReadFile(fileName)