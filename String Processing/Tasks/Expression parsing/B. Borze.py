# string = input()
string = input()
dic = {".": '0',
       "-.": "1",
       "--": "2"}
count = 0
res = ''
while count < len(string):
    if string[count:count+2] in {"-.", "--"}:
        res += dic[string[count:count+2]]
        count += 2
    elif string[count:count+1] == ".":
        res += dic[string[count:count+1]]
        count += 1
    else:
        count += 1
print(res)
