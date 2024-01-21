# l=list()
# cnt=0
n=int(input("Enter value of n: "))
# for i in range(0,n):
#     s=input("Enter name: ")
#     l.append(s)
# print(l)
# j=0
# for j in l:
#     if (j.__contains__('patel')):
#         cnt+=1
# print(cnt) 

list=[]
cnt=0
i=0
for i in range(0,n):
    s=input("Enter name: ")
    list.insert(i,s)
    if(list[i].__contains__('patel')):
        cnt+=1
print(cnt)

