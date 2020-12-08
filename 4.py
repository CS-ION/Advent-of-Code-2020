import re

f = open('input.txt','r')
L = f.read().split('\n\n')

valid_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
part1 = 0
valid = 0
tot_pass = len(L)

def check1(val):
    for I in val:
        if I.isdigit() or (ord(I) in [x for x in range(97,103)]) :
            pass
        else:
            return False
    return True

def check2(val):
    if 'cm' in Y['hgt']:
        P = Y['hgt'].split('cm')[0]
        if int(P) in [I for I in range(150,194)]:
            return True
    elif 'in' in Y['hgt']:
        P = Y['hgt'].split('in')[0]
        if int(P) in [I for I in range(59,77)]:
            return True
    return False

for I in range(tot_pass):

    X = re.split(' |\n',L[I])
    Y = {}
    for J in X:
        Y[J.split(':')[0]] = J.split(':')[1]
    
    if all(key in Y for key in valid_fields):
        part1 += 1
 
        a=int(Y['byr']) in [I for I in range(1920,2003)]
        b=int(Y['iyr']) in [I for I in range(2010,2021)]
        c=int(Y['eyr']) in [I for I in range(2020,2031)]            
        d= Y['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        e= Y['hcl'][0]=='#' and len(Y['hcl'])==7 and check1(Y['hcl'][1::])                       
        f=(len(Y['pid'])==9) 
        g = check2(Y['hgt'])

        if all([a,b,c,d,e,f,g])==True:
            valid+=1

print('Part1',part1)
print('Part2',valid)
