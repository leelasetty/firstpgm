
a = '20'
b = 12
str_s=99
float_f1=12.4
sum = a + str(b)
print (sum)

list_l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list_l1[:18])
list_l1.append(121)
print(list_l1)
list_l1.pop()
print(list_l1)

list_l2 = []
for i in range(56):
    list_l2.append(i)
print(list_l2)



def adding(a, b):
    str_s1="I am"
    str_s2="learing python"
    print(str_s1+str_s2)
    return (str_s1+str_s2+' '+a)

print(adding('welcome', 31))