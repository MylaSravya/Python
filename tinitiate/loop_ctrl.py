
# Break
"""
for c in range(5): # 0,1,2,3,4
    if c == 3:
        break
    print(c)

print(12)


for c1 in range(5):
    if c1 == 3:
        break
    for c2 in range(5):
        if c2 == 3:
            break
        print(c1,c2)
    # if c1 == 3:
    #    break


for c in range(3):
    print('Run:', c,'step1')
    if c==1:
        continue
        # break
    print('Run:', c,'step2')
    print('Run:', c,'step3')
"""

for c in range(3):
    pass
    if c==1:
        print('Do a very important step')
    elif c==2:
        pass # DO NOTHING
    else:
        print('normal processing')
