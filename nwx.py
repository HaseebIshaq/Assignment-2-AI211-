import networkx as nx
import matplotlib.pyplot as plt


def show_wgraph():
    plt.figure()
    pos = nx.spring_layout(G)
    weight_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, font_color='white', node_shape='s', with_labels=True,)
    output = nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels)
    plt.show()


G = nx.DiGraph()

G.add_node('Orandea')
G.add_node('Zerind')
G.add_node('Arad')
G.add_node('Timisoara')
G.add_node('Lugoj')
G.add_node('Mehadia')
G.add_node('Dobreta')
G.add_node('Sibiu')
G.add_node('Rimnicu Vilcea')
G.add_node('Fagaras')
G.add_node('Pitesti')
G.add_node('Craiova')
G.add_node('Bucharest')
G.add_node('Giurgiu')
G.add_node('Urziceni')
G.add_node('Hirsova')
G.add_node('Eforie')
G.add_node('Vaslui')
G.add_node('Iasi')
G.add_node('Neamt')

G.add_edge('Oradea', 'Zerind', weight=71)
G.add_edge('Zerind', 'Arad', weight=75)
G.add_edge('Arad', 'Timisoara', weight=118)
G.add_edge('Oradea', 'Sibiu', weight=151)
G.add_edge('Arad', 'Sibiu', weight=140)
G.add_edge('Arad', 'Timisoara', weight=118)
G.add_edge('Timisoara', 'Lugoj', weight=111)
G.add_edge('Lugoj', 'Mehadia', weight=70)
G.add_edge('Mehadia', 'Dobreta', weight=75)
G.add_edge('Dobreta', 'Craiova', weight=120)
G.add_edge('Craiova', 'Rimnicu Vilcea', weight=146)
G.add_edge('Craiova', 'Pitesti', weight=138)
G.add_edge('Rimnicu Vilcea', 'Pitesti', weight=97)
G.add_edge('Sibiu', 'Fagaras', weight=99)
G.add_edge('Sibiu', 'Rimnicu Vilcea', weight=80)
G.add_edge('Fagaras', 'Bucharest', weight=211)
G.add_edge('Pitesti', 'Bucharest', weight=101)
G.add_edge('Bucharest', 'Giurgiu', weight=90)
G.add_edge('Bucharest', 'Urziceni', weight=85)
G.add_edge('Urziceni', 'Vaslui', weight=142)
G.add_edge('Vaslui','Iasi', weight=92)
G.add_edge('Iasi', 'Neamt', weight=87)
G.add_edge('Urziceni', 'Hirsova', weight=98)
G.add_edge('Hirsova', 'Eforie', weight=86)

show_wgraph()