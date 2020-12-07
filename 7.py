f = open('input.txt','r')
L = f.read().split('\n')

gold_bags = [I.split(' ')[0]+' '+I.split(' ')[1] for I in L if 'shiny gold' in I and I.split(' ')[0]+' '+I.split(' ')[1]!='shiny gold']

contain = []
while gold_bags:
    bag = gold_bags.pop()
    if bag in contain:
        continue
    contain.append(bag)
    new_bags = [I.split(' ')[0]+' '+I.split(' ')[1] for I in L if bag in I and I.split(' ')[0]+' '+I.split(' ')[1]!=bag]
    gold_bags+=new_bags

print('Part1',len(contain))

import re

def contain_bags(colour):
    line = [I for I in L if I.split(' ')[0]+' '+I.split(' ')[1]==colour]
    bag = re.split('contain |, ',line[0])
    t = 1
    for I in bag[1::]:
        I = I.split(' ')
        if I[0]!='no':
            t += int(I[0]) * contain_bags(I[1]+' '+I[2])
    return t

print('Part2',contain_bags('shiny gold')-1)
