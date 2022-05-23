import string

s = string.ascii_lowercase
n = eval(input())

with open(r'./The Old Man and the Sea.txt') as file:
    text = file.readlines()
n = min(n, len(text))
myStr = ''.join(text[:n])
ls = [[x, myStr.lower().count(x)] for x in s]
ls.sort(key = lambda x : (-x[1], x[0]))
for i in ls:
    print('{} 的数量是 {:>3} 个'.format(i[0], i[1]))