# income = [0.1, 0.05, 0.04, 0.03, 0.02]
# price,*friend_per_lvl = [float(input()) for _ in range(6)]
# price *= 0.93
# without_tax = (sum(price * j for j in(income[k]*friend_per_lvl[k] for k in range(len(friend_per_lvl)))))
# print(199.2/(without_tax - without_tax*0.1))



# a = [1499, 500, 300]
# b = 500 *0.83*0.05
# c = [200, 500, 1499 ]
# d = 1499*0.83*0.03
# e = [300, 345, 541]
# a = sum([i*0.83*0.1 for i in a])
# c = sum([i*0.83*0.04 for i in c])
# e = sum([i*0.83*0.02 for i in e])
# print(sum([a,b,c,d,e]))

# a = 'False'
# a = a.replace("'","")
# print(a)as
# print(' '.join((input().split())))

#
# a1,a2,a3,a4,a5=[1499, 500, 300], [500],[200, 500, 1499], [1499], [300, 345, 541]
# for i in range(len(a1)):
#     a1[i]=float(a1[i])
#
# for i in range(len(a2)):
#     a2[i]=float(a2[i])
# for i in range(len(a3)):
#     a3[i]=float(a3[i])
# for i in range(len(a4)):
#     a4[i]=float(a4[i])
# for i in range(len(a5)):
#     a5[i]=float(a5[i])
# print(a1,a2,a3,a4,a5)
# print(sum(a1)*0.83*0.1, sum(a2)*0.83*0.05,sum(a3)*0.83*0.04,sum(a4)*0.83*0.03,sum(a5)*0.83*0.02)
# print(0.83*sum(a1)*0.1+0.83*sum(a2)*0.05+0.83*sum(a2)*0.04+0.83*sum(a2)*0.03+0.83*sum(a2)*0.02)