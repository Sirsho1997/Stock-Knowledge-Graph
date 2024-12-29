"""
This script visualizes the graph representing stocks
"""
import json
import networkx as nx
from pyvis.network import Network
import os

def visualize():

    # Load the JSON file containing the graph
    with open('graph_data/graph_data.json', 'r') as file:
        data = json.load(file)

    nodes = data['nodes']
    links = data['links']

    # Generating the graph
    G = nx.Graph()
    for node in nodes:
        G.add_node(node['label'])

    for link in links:
        G.add_edge(link['source'], link['target'])

    # Defining setting for visualization
    g = Network(notebook=False, cdn_resources='remote')
    g.from_nx(G)

    # Extracting different sector names that will help in assigning color
    with open('scraped_data/sector_ticker_dict.json', 'r') as file:
        sector_data = json.load(file)

    # Assigining color to nodes
    for node in g.nodes:

        if node['label'] == 'Stock':
            node['color'] = '#c0c236 '
        if 'Symbol' in node['label']:
            node['color'] = '#2fbd9d '
        if '(' in node['label']:
            node['color'] = '#da9cd7'
        if node['label'] in sector_data.keys():
            node['color'] = '#86eacc'


    with open('07_graph_data_pyvis.html', 'w') as fp:
        fp.write(g.generate_html())


if __name__ == "__main__":

    visualize()

