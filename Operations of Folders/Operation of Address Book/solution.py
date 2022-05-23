def ReadFile():
    with open("./info.csv", 'r', encoding='GBK') as file:
        for lines in file:
            tr = lines.strip().split(',')
            dic[tr[0]] = tr[1:]


def show():
    for name, value in dic.items():
        print(name, value[0], value[1])


if __name__ == '__main__':
    dic = {}
    ReadFile()
    c = input()
    if c == 'A':
        show()
    elif c == 'D':
        print(dic)
    else:
        print("ERROR")