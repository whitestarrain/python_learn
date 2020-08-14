# import keyword
# arr=[1,2,3,4,"bad"]
# print(arr.count(2))
# print(arr.__len__())
# print(arr.index('bad'))
# print(arr.index(2,1))
# arr2=[2,3,4,4,"123123"]
# arr2.extend(arr)
# print(arr2)
# arr.append(arr2)
# print(arr)

# del arr[2]

# len(arr)
# arr.__len__()
# print(type(keyword.kwlist))

# for a in arr:
#     print(a,end=" ")

t = ("zhangsan", 175.7,18)
print(t[0])
print(len(t))
print(t)
print(type(t))

print("名字：%s，身高:%.2f,年龄：%d" % t)

str="dfadf"
map={
    "name":1,
    "value":"value1",
    str:str
}
print(map)
print(id(str),id(map.get(str)))

for k in map:
    print(k,':',map.get(k))

print('afajsf"asfasf"fa;ofhwa')
print("aaabbbaaabbbaa".center(20,'c'))
print(str.isspace())

print("dddddd".replace('d','1',2))

print([1,2,3,4][-1])

print((1,1,1,1)+(2,2,2,2))
print([1,2,3,4,5][1:3])
print([0,1,2,3,4,5,6,7][0::2])

print(list(range(10)))

print([1,2,3,4]*5)

l=[1,2,3,4]
def ftest(l):
    l.append(5)
ftest(l)
print(l)