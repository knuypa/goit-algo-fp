import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import matplotlib.colors as mcolors
import numpy as np

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, label=node.val)
        pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def dfs_visit(node, order, order_dict):
    if node:
        order.append(node.id)
        order_dict[node.id] = len(order)
        dfs_visit(node.left, order, order_dict)
        dfs_visit(node.right, order, order_dict)

def bfs_visit(root, order, order_dict):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            order.append(node.id)
            order_dict[node.id] = len(order)
            queue.append(node.left)
            queue.append(node.right)

def draw_tree(tree_root, pos, colors, labels):
    plt.figure(figsize=(8, 5))
    nx.draw(tree_root, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def visualize_tree_traversal(tree_root):
    tree = nx.DiGraph()
    pos = {}
    add_edges(tree, tree_root, pos, 0, 0)
    
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes}

    # DFS Visualization
    dfs_order = []
    dfs_dict = {}
    dfs_visit(tree_root, dfs_order, dfs_dict)
    dfs_colors = [mcolors.to_hex(c) for c in plt.cm.Blues(np.linspace(0.3, 1, len(dfs_order)))]
    dfs_color_map = {node: dfs_colors[dfs_dict[node] - 1] for node in dfs_order}
    draw_tree(tree, pos, [dfs_color_map[node] for node in tree.nodes], labels)

    # BFS Visualization
    bfs_order = []
    bfs_dict = {}
    bfs_visit(tree_root, bfs_order, bfs_dict)
    bfs_colors = [mcolors.to_hex(c) for c in plt.cm.Greens(np.linspace(0.3, 1, len(bfs_order)))]
    bfs_color_map = {node: bfs_colors[bfs_dict[node] - 1] for node in bfs_order}
    draw_tree(tree, pos, [bfs_color_map[node] for node in tree.nodes], labels)

# Створення та візуалізація дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

visualize_tree_traversal(root)