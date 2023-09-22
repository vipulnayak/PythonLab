def roman2dec(str):
  romandict={'I':1,'v':5,'x':10,'L':50,'C':100,'D':500,'M':100}
  romanback=list(str)[::-1]
  value=0
  rival=romandict[romanback[0]]
  for numeral in romanback:
    leval=romandict[numeral]
    if leval <rival:
        value-=leval
    else:
        value+=leval
    rival=leval
  return value
str=input("enter the roman number \n" )
print("Decimal number :",roman2dec(str))