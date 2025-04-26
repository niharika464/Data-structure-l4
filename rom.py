def roman_to_int(z):
    roman={'V':5, 'X':10, 'L':50, 'C':100}
    intg=0
    for i in range(len(z)):
        if i+1<len(z) and roman[z[i]]<roman[z[i+1]]:
                 intg=roman[z[i]]
        else:
              intg+=roman[z[i]]
              return intg
z=input("enter a roman number:")
print(roman_to_int(z))        