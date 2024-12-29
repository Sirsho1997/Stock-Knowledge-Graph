"""
This script generates the graph representing stocks
"""

import networkx as nx
import json
import os
# Save the graph to a JSON file
def save_graph_to_json(graph, filename):
    """
    Saves the NetworkX graph to a JSON file.

    Args:
        graph: The NetworkX graph object.
        filename: The name of the output JSON file.
    """

    data = nx.readwrite.json_graph.node_link_data(graph, edges="links")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def create_graph(relationships):
    """
    Creates a graph representing stock relationships with sectors and companies,
    including separate nodes for each technical indicator (RSI, SMA, SAR) with 3 days of data.

    Args:
        relationships: A dictionary representing stock relationships,along with indicators

    Returns:
        A networkx graph representing the relationships.
    """

    G = nx.DiGraph()

    for stock, sectors in relationships.items():
        # Start with the root node 'Stock'
        G.add_node(stock, label=stock, color="blue", hidden=False)
        for sector, companies in sectors.items():
            # Looping each Sectors for stocks
            G.add_node(sector, label=sector, color="blue", hidden=False)
            G.add_edge(stock, sector)
            for company, indicators in companies.items():
                # Looping Stocks representing the Sector
                G.add_node(f"Symbol: {company}", label=f"Symbol: {company}", color="blue", hidden=False)
                G.add_edge(sector, f"Symbol: {company}")

                for day, data in indicators.items():
                    # Looping Date of the Indicator
                    day = day.split("Day ")[-1]

                    G.add_node(f"{company} {day}", label=f"{company} {day}", color="blue", hidden=False)
                    G.add_edge(f"Symbol: {company}", f"{company} {day}")

                    for indic, value in data.items():
                        # Indicator Values such as (RSI, SMA, SAR)
                        G.add_node(f"{company} ({indic}) : {round(value,2)}", label=f"{company} ({indic}) : {round(value,2)}", color="lavender", hidden=False)
                        G.add_edge(f"{company} {day}", f"{company} ({indic}) : {round(value,2)}")

    return G

def main_run():

    os.makedirs('graph_data', exist_ok=True)
    with open("graph_data/stock_relationships.json", "r") as f:
        relationships = json.load(f)

    G = create_graph(relationships)

    save_graph_to_json(G, "graph_data/graph_data.json")

if __name__ == "__main__":
    main_run()
