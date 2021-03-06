from file_interface import read_file, write_file
from utils import process_map, extract_developers
from graph import extract_graph
import numpy as np
from multiprocessing import Pool


files = ['a_solar.txt', 'b_dream.txt', 'c_soup.txt', 'd_maelstrom.txt', 'e_igloos.txt', 'f_glitch.txt']
# for file in files:
#     read_file(file)
info, companies = read_file(files[0])
map = info['map']
G, components = extract_graph(map)
print(G, components)
PM, DE = process_map(map)

pms = info['pms']
pms.sort(key=lambda x:(companies[x['company']], x['bonus']), reverse=True)
developers = info['developers']
developers.sort(key=lambda x: x['n_skills'], reverse=True)

dev_companies = extract_developers(developers, companies)

for c, dev in dev_companies.items():
    dev.sort(key=lambda x:x['bonus']+x['n_skills'], reverse=True)

output = {}
output['developers'] = info['developers']
output['pms'] = info['pms']
# write_file(files[0].split('.txt')[0]+"_out.txt", output)

added_pms = set()
added_dev = set()

visited_nodes = {}


for c in components:
    for node in c:
        if node[2] == "M" and node not in visited_nodes:

            pms[0]['pos'] = (node[0], node[1])
            visited_nodes[node] = pms[0]

            added_pms.add(pms[0])
            current_pm = pms[0]
            pms.pop(0)

            for adj_node in G.neighbors(node):
                if adj_node[2] != "M" and adj_node not in visited_nodes:
                    dev = dev_companies[current_pm['company']][0]
                    dev['pos'] = (adj_node[0], adj_node[1])
                    visited_nodes[adj_node] = dev
                    added_dev.add(dev['id'])

    while len(visited_nodes) <= len(c):
            for node in c:
                if node in visited_nodes:
                    current_node = visited_nodes[node]
                    for adj_node in G.neighbors(node):
                        if adj_node[2] != "M" and adj_node not in visited_nodes:
                            visited_nodes[adj_node] =
                            dev = dev_companies[current_node['company']][0]









