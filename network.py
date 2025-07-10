import networkx as nx
from pyvis.network import Network
from db import fetch_all_dreams

def build_network():
    try:
        dreams = fetch_all_dreams()
        print(f"[DEBUG] Number of dreams fetched: {len(dreams)}")
    except Exception as e:
        print(f"[DB ERROR] Failed to fetch dreams: {e}")
        dreams = []
    G = nx.Graph()

    for dream in dreams:
        G.add_node(dream[0], title=dream[1], keywords=dream[6])

    for i in range(len(dreams)):
        for j in range(i + 1, len(dreams)):
            keywords1 = set(dreams[i][6].split(', '))
            keywords2 = set(dreams[j][6].split(', '))
            common = keywords1.intersection(keywords2)
            if len(common) >= 2:
                G.add_edge(dreams[i][0], dreams[j][0], weight=len(common))

    net = Network(height="600px", width="100%", notebook=False)
    net.from_nx(G)
    net.save_graph("dream_network.html")
