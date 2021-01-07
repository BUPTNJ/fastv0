import re
import collections
from graphviz import Digraph

forward = collections.defaultdict(set)

def make_topo_dict(f_name):
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

def make_topo_ficture(forward):
    dot = Digraph(name="topo", comment="traceroute", format="png")
    ip_set = set()
    for k,v in forward.items():
        ip_set.add(k)
        for ip in v:
            ip_set.add(ip)
    for ip in ip_set:
        dot.node(name=ip, label=ip, color='black')
    for k,v in forward.items():
        for ip in v:
            dot.edge(k,ip)
    dot.view(filename="mypicture", directory="D:\MyTest")

    # 跟view一样的用法(render跟view选择一个即可)，一般用render生成图片，不使用view=True,view=True用在调试的时候
    dot.render(filename='topo', directory="./",view=True)
make_topo_ficture(make_topo_dict('北京_trace_龙岩'))