def process_map(map):
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
    return PM, DE

def extract_developers(developers, companies):
    dev_companies = {}
    for comp in companies.keys():
        for dev in developers:
            if dev['company'] == comp:
                if comp not in dev_companies:
                    dev_companies[comp] = []
                dev_companies[comp].append(dev)
    return dev_companies