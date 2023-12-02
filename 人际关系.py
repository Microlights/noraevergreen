import networkx as nx

def find_shortest_path(graph, start, end):
    try:
        shortest_path = nx.shortest_path(graph, source=start, target=end)
        return shortest_path
    except nx.NetworkXNoPath:
        return None

# 创建一个简单的人际关系网络
G = nx.Graph()
G.add_edges_from([
    ('Alice', 'Bob'),
    ('Bob', 'Charlie'),
    ('Charlie', 'David'),
    ('David', 'Eve'),
    ('Eve', 'Frank'),
    ('Frank', 'Grace'),
    ('Grace', 'Alice'),
])

# 查找两个人之间的最短路径
start_person = 'Alice'
end_person = 'David'
shortest_path = find_shortest_path(G, start_person, end_person)

if shortest_path:
    print(f"最短路径从 {start_person} 到 {end_person} 是: {shortest_path}")
else:
    print(f"无法找到从 {start_person} 到 {end_person} 的路径")
