

kw = input('请输入要检索的关键字:')
with open('getdata.txt', 'r') as file:
    lines = file.readlines()
    regex = str(kw)
    for line in lines:
        if regex in line:
            print(line)





