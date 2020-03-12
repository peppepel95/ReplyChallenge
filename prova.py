from file_interface import read_file, write_file
import numpy as np
from multiprocessing import Pool


files = ['a_solar.txt', 'b_dream.txt', 'c_soup.txt', 'd_maelstrom.txt', 'e_igloos.txt', 'f_glitch.txt']
# for file in files:
#     read_file(file)
info, companies = read_file(files[0])

print(info)
print(companies)
map = info['map']

r_index = 0
c_index = 0
PM = []
DE = []
for r in map:
    for c in r:
        coor = (r_index, c_index)
        if c == 'M':
            PM.append(coor)
        if c == '_':
            DE.append(coor)
        c_index += 1
    r_index += 1

print(PM)
print(DE)

pms = info['pms']
pms.sort(key=lambda x:(companies[x['company']], x['bonus']), reverse=True)
print(pms)

developers = info['developers']
developers.sort(key=lambda x:x['n_skills'], reverse=True)
print(developers)

dev_companies = {}
for comp in companies.keys():
    for dev in developers:
        if dev['company'] == comp:
            if comp not in dev_companies:
                dev_companies[comp] = []
            dev_companies[comp].append(dev)

print(dev_companies)