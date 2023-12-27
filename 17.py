def perm3(s1):
    i=0
    list1=[]
    list1.append(s1[i]+s1[i+1]+s1[i+2])
    list1.append(s1[i]+s1[i+2]+s1[i+1])
    list1.append(s1[i+1]+s1[i]+s1[i+2])
    list1.append(s1[i+1]+s1[i+2]+s1[i])
    list1.append(s1[i+2]+s1[i]+s1[i+1])
    list1.append(s1[::-1])
    return list1

def perm4(s2):
    
    list4=[]
    part1=s2[0]
    part2=s2[1:4]
    list1=(perm3(part2))
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    part1=s2[1]
    part2=s2[0]+s2[2]+s2[3]
    list1=(perm3(part2))
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    part1=s2[2]
    part2=s2[0]+s2[1]+s2[3]
    list1=(perm3(part2))
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    part1=s2[3]
    part2=s2[0]+s2[1]+s2[2]
    list1=(perm3(part2))
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    return list4
s2="FAST"
list4=perm4(s2)
print(list4)







