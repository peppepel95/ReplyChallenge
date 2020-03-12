from file_interface import read_file, write_file
from utils import process_map, extract_developers
import numpy as np
from multiprocessing import Pool


files = ['a_solar.txt', 'b_dream.txt', 'c_soup.txt', 'd_maelstrom.txt', 'e_igloos.txt', 'f_glitch.txt']
# for file in files:
#     read_file(file)
info, companies = read_file(files[0])
map = info['map']

PM, DE = process_map(map)

pms = info['pms']
pms.sort(key=lambda x:(companies[x['company']], x['bonus']), reverse=True)
developers = info['developers']
developers.sort(key=lambda x:x['n_skills'], reverse=True)

dev_companies = extract_developers(developers, companies)

output = {}
output['developers'] = info['developers']
output['pms'] = info['pms']
# write_file(files[0].split('.txt')[0]+"_out.txt", output)