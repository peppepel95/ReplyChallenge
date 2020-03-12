def read_file(filename):
    with open(filename, "r") as f:
        content = f.read()
        info = {}
        part1 = content.split("\n")
        part2 = part1[0].split(" ")
        info['width'] = int(part2[0])
        info['height'] = int(part2[1])
        map = ""
        for i in range(1, info['height']+1):
            map += part1[i]+"\n"
        map_list = []
        for line in map.split("\n"):
            if line != "":
                row = []
                for c in line:
                    row.append(c)
                map_list.append(row)
        info['map'] = map_list
        part1 = part1[info['height']+1:]
        info['n_devs'] = int(part1[0])
        part1 = part1[1:]
        developers = []
        companies = {}
        for i in range(info['n_devs']):
            developer = {}
            data = part1[i].split(" ")
            company = data[0]
            if company not in companies.keys():
                companies[company] = 0
            developer['company'] = company
            companies[company] += 1
            developer['bonus'] = int(data[1])
            developer['n_skills'] = int(data[2])
            developer['skills'] = []
            for j in range(developer['n_skills']):
                developer['skills'].append(data[2+j])
            developers.append(developer)
        info['developers'] = developers
        part1 = part1[info['n_devs']:]
        info['n_pms'] = int(part1[0])
        part1 = part1[1:]
        pms = []
        for i in range(info['n_pms']):
            pm = {}
            data = part1[i].split(" ")
            pm['company'] = data[0]
            pm['bonus'] = int(data[1])
            pms.append(pm)
        info['pms'] = pms

        return info, companies


def write_file(filename, output):
    with open(filename, 'w') as f:
        f.write(str(output['n_libreries'])+"\n")
        for key, value in output['libreries'].items():
            f.write(str(key)+" "+str(len(value))+"\n")
            i = 0
            for elem in value:
                f.write(str(elem))
                if i == len(value)-1:
                    f.write("\n")
                    break
                else:
                    f.write(" ")
                i += 1