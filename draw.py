from utility import make_topo_dict
from graphviz import Digraph

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

make_topo_ficture(make_topo_dict('./北京_trace/北京_trace_龙岩'))