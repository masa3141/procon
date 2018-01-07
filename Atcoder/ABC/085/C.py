# -*- coding: utf-8 -*-

N, Y = map(int, input().split())

moneys = [10000, 5000, 1000]

man = 0
gosen = 0
sen = 0
'''
方針：とりあえず、できるかの計算
その後は、１万円札から５０００円に両替
その次に５０００円札を１００００円に両替していく
'''

while Y > 0:
    if Y//10000 > 0:
        man += 1
        Y -= 10000
    elif Y//5000 > 0:
        gosen += 1
        Y -= 5000
    else:
        sen += 1
        Y -= 1000

if Y != 0 or (man+gosen+sen > N):
    print(-1, -1, -1)
    exit()


diff = N - (man+gosen+sen)
# print(man+gosen+sen, N)
# print("a",diff)
gosen_to_sen = min(diff//4, gosen)
gosen -= gosen
sen += 5*gosen_to_sen
diff = N - (man+gosen+sen)

man_to_sen = min(diff//9, man)
man -= man_to_sen
sen += 10*man_to_sen
diff = N - (man+gosen+sen)
#print(man, gosen, sen)

# print(man, gosen, sen)
man_to_gosensen = min(diff//5, man)
man -= man_to_gosensen
gosen += 1*man_to_gosensen
sen += 5*man_to_gosensen
diff = N - (man+gosen+sen)

man_to_gosen = min(diff, man)
man -= man_to_gosen
gosen += 2*man_to_gosen
diff = N - (man+gosen+sen)
# print(man, gosen, sen)
gosen_to_sen = min(diff//4, gosen)
gosen -= gosen
sen += 5*gosen_to_sen
diff = N - (man+gosen+sen)

# while diff != 0:
#     if man+gosen+sen == N:
#         print(man, gosen, sen)
#         exit()
#     else:
#         if man > 0:
#             man -= 1
#             # gosen += 2
#             sen
#         elif gosen > 0:
#             gosen -= 1
#             sen += 5

if man+gosen+sen == N:
    print(man, gosen, sen)
else:
    print(-1, -1, -1)
