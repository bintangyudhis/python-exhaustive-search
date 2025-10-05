import itertools
import networkx as nx
import matplotlib.pyplot as plt

# 1. Node dan Bobot Jarak
nodes = ['Q','R','S','T','U','P']
w = {
    ('Q','R'):5, ('Q','S'):3, ('Q','T'):6, ('Q','U'):7, ('Q','P'):4,
    ('R','S'):9, ('R','T'):4, ('R','U'):8, ('R','P'):6, ('R','Q'):5,
    ('S','T'):3, ('S','U'):5, ('S','P'):8, ('S','Q'):3, ('S','R'):9,
    ('T','U'):6, ('T','P'):7, ('T','Q'):6, ('T','R'):4, ('T','S'):3,
    ('U','P'):2, ('U','Q'):7, ('U','R'):8, ('U','T'):6, ('U','S'):5,
    ('P','Q'):4, ('P','R'):6, ('P','S'):8, ('P','T'):7, ('P','U'):2
}

# Pastikan bobot simetris
for a in nodes:
    for b in nodes:
        if a == b:
            continue
        if (a,b) in w and (b,a) not in w:
            w[(b,a)] = w[(a,b)]

# 2. Buat Graph
G = nx.Graph()
G.add_nodes_from(nodes)
for (a,b), d in w.items():
    if a < b:
        G.add_edge(a, b, weight=d)

# 3. Posisi node
pos = {
    'R': (-2.5, 2.2),    # Kiri atas (Futsal)
    'U': (1.2, 1.9),     # Tengah-kanan atas (Freelance)
    'T': (-3.5, 0.4),    # Kiri tengah, vertikal dengan R (Nugas)
    'P': (1.2, 0.6),     # Tengah kanan (Kos)
    'S': (4.8, 0.4),     # Paling kanan (Kopi)
    'Q': (-0.8, -1.8)    # Bawah tengah agak ke kiri (Kampus)
}
# 4. Cetak Matriks Jarak
order = ['Q','R','S','T','U','P']
print("Matriks jarak")
header = "    " + " ".join(f"{x:>3}" for x in order)
print(header)
for i in order:
    row = [i]
    for j in order:
        row.append(0 if i == j else G[i][j]['weight'])
    print(f"{i:>3} " + " ".join(f"{v:>3}" for v in row[1:]))
print()

# 5. Hitung Rute Terpendek dari Q (TSP)
start = 'Q'
others = [n for n in order if n != start]
best_route = None
best_cost = float('inf')

def d(a,b):
    return G[a][b]['weight']

for perm in itertools.permutations(others):
    route = [start] + list(perm) + [start]
    cost = sum(d(route[i], route[i+1]) for i in range(len(route)-1))
    route_str = " -> ".join(route)
    print(f"{route_str} = {cost}")
    if cost < best_cost:
        best_cost = cost
        best_route = route

print()
print("Rute tercepat:", " -> ".join(best_route))
print("Total jarak:", best_cost)
print()

# 6. Visualisasi Sebelum
plt.figure(figsize=(8,6))
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="#b8d8ff")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
nx.draw_networkx_edges(G, pos, width=1.2, alpha=0.6)
edge_labels = {(u,v): G[u][v]['weight'] for u,v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.title("Sebelum: Semua Koneksi")
plt.axis('off')

# 7. Visualisasi Sesudah
plt.figure(figsize=(8,6))
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="#b8d8ff")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
nx.draw_networkx_edges(G, pos, width=1, alpha=0.2)

# Rute terbaik disorot
best_edges = [(best_route[i], best_route[i+1]) if best_route[i] < best_route[i+1]
              else (best_route[i+1], best_route[i]) for i in range(len(best_route)-1)]
nx.draw_networkx_edges(G, pos, edgelist=best_edges, width=3.0, edge_color="blue")
edge_labels_best = {e: G[e[0]][e[1]]['weight'] for e in best_edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels_best, font_size=9)
plt.title("Sesudah: Rute Tercepat Disorot")
plt.axis('off')

plt.tight_layout()
plt.show()
