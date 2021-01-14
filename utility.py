import collections
import re

def make_topo_dict(f_name):
    forward = collections.defaultdict(set)
    file = open(f_name)
    last_hop = ""
    next_hop = ""
    while True:
        line = file.readline()
        if not line:
            break
        if 'traceroute' in line:
            last_hop = re.findall('traceroute from (.*) to .*',line)[0]
        else:
            if 'ms' in line:
                #非匿名
                next_hop = line.split()[1]
                if last_hop != "" :
                    forward[last_hop].add(next_hop)
                last_hop = next_hop
            else:
                last_hop = ""
                pass
    return forward