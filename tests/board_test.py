a = []

for i in range(64):
    if i == 27 or i == 36:
         a.append('◎')
    elif i == 28 or i == 35:
         a.append('●')
    else:
         a.append('□')

print(' ',1,2,3,4,5,6,7,8)
for j in range(0, 63, 8):
    print(j//8+1,*a[j:j+8])