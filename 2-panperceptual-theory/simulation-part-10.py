import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.patches import Circle

# Initialize an empty graph
G = nx.Graph()

# Add the central node representing the "Nucleus" or "Central Perception" of the perceptual atom
G.add_node("Nucleus", layer=0, concept="Central Perception")

# Define the parameters for the different "orbits" or perceptual layers of the atom
num_orbits = 3 # Total number of layers (Sensory, Cognitive, Physical)
nodes_per_orbit = [4, 6, 8] # Number of nodes in each orbit
orbit_radii = [1.5, 3, 4.5] # Radii for each orbit in the visualization
orbit_labels = ["Sensory", "Cognitive", "Physical"] # Labels for the orbits
orbit_concepts = [
    ["Vision", "Hearing", "Touch", "Smell"], # Concepts for the Sensory orbit
    ["Memory", "Attention", "Processing", "Analysis", "Integration", "Recognition"], # Concepts for the Cognitive orbit
    ["Response", "Action", "Feedback", "Adaptation", "Learning", "Expression", "Communication", "Decision"] # Concepts for the Physical orbit
]
orbit_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1'] # Distinctive colors for each orbit

# Dictionary to store additional information for each node (concept, layer, color)
node_info = {}

# Loop to add nodes to each orbit and connect them to the nucleus
for orbit, (n_nodes, radius, label, concepts, color) in enumerate(
    zip(nodes_per_orbit, orbit_radii, orbit_labels, orbit_concepts, orbit_colors),
    start=1): # 'start=1' so layers begin from 1 (not 0)
    for i in range(n_nodes):
        # Calculate the position of each node on a circle (orbit)
        angle = 2 * np.pi * i / n_nodes
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        node_id = f"{label[0]}{i+1}" # Generate a node ID like S1, C1, F1, etc.
        concept = concepts[i] if i < len(concepts) else f"{label} {i+1}" # Assign a concept to the node
        # Add the node to the graph with its position, layer, concept, and color
        G.add_node(node_id, pos=(x, y), layer=orbit, concept=concept, color=color)
        # Add an edge (connection) between the Nucleus and the current node
        G.add_edge("Nucleus", node_id)
        # Store the node's information in the 'node_info' dictionary
        node_info[node_id] = {'concept': concept, 'layer': orbit, 'color': color}

# Define "resonance" connections between nodes of different orbits
inter_connections = [
    ("S1", "C1"), ("S2", "C2"), ("C3", "F1"), ("C4", "F2"), ("F3", "C5")
]
# Add these connections to the graph
for conn in inter_connections:
    if conn[0] in G.nodes() and conn[1] in G.nodes(): # Ensure the nodes exist
        G.add_edge(conn[0], conn[1])

# Get the positions of all nodes in the graph for visualization
pos = nx.get_node_attributes(G, 'pos')
pos["Nucleus"] = (0, 0) # Ensure the Nucleus is at the center (0,0)

# Create the graph visualization
fig, ax = plt.subplots(figsize=(8, 8))

# Draw the circles representing the orbits
for i, radius in enumerate(orbit_radii):
    circle = Circle((0, 0), radius, fill=False, linestyle='--', alpha=0.3,
                    color=orbit_colors[i], linewidth=1.5)
    ax.add_patch(circle)

# Draw the nodes
# Nucleus node
nx.draw_networkx_nodes(G, pos, nodelist=["Nucleus"], node_size=500,
                       node_color='gold', edgecolors='black', linewidths=1.5, ax=ax)
# Orbit nodes (Sensory, Cognitive, Physical)
for orbit in range(1, num_orbits + 1):
    orbit_nodes = [n for n in G.nodes() if G.nodes[n].get('layer') == orbit]
    if orbit_nodes:
        colors = [G.nodes[n]['color'] for n in orbit_nodes]
        nx.draw_networkx_nodes(G, pos, nodelist=orbit_nodes, node_size=300,
                               node_color=colors, edgecolors='black', linewidths=1, ax=ax)

# Draw the edges (connections)
# Radial edges (from Nucleus to orbit nodes)
radial_edges = [(u, v) for u, v in G.edges() if "Nucleus" in [u, v]]
nx.draw_networkx_edges(G, pos, edgelist=radial_edges, alpha=0.5, width=1,
                       edge_color='gray', ax=ax)
# Resonance edges (between nodes of different orbits)
resonance_edges = [(u, v) for u, v in G.edges() if "Nucleus" not in [u, v]]
nx.draw_networkx_edges(G, pos, edgelist=resonance_edges, alpha=0.7, width=1.5,
                       edge_color='red', style='dashed', ax=ax)

# Add labels to the nodes (node IDs)
nx.draw_networkx_labels(G, pos, font_size=6, font_family='serif',
                         font_weight='bold', ax=ax)

# Create a legend for the plot
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=f"Orbit {i+1}: {label}")
                   for i, (label, color) in enumerate(zip(orbit_labels, orbit_colors))]
legend_elements.append(Patch(facecolor='gold', label="Nucleus: Central Perception"))
legend_elements.append(plt.Line2D([0], [0], color='red', linestyle='--',
                                  label="Resonance Connections"))
ax.legend(handles=legend_elements, loc='upper right',
          bbox_to_anchor=(1.12, 1), fontsize=7)

# Set the title and layout adjustments for the plot
plt.title("Perceptual Resonance Atomic Model (PRAM)\nA Multi-Layered Cognitive Architecture",
          fontsize=12, fontweight='bold', pad=10, fontfamily='serif')
ax.set_xlim(-5, 5) # Set X-axis limits
ax.set_ylim(-5, 5) # Set Y-axis limits
ax.set_aspect('equal') # Ensure axes have the same scale
ax.axis('off') # Hide the axes

# Add text annotations at the bottom left of the plot
ax.text(-4.5, -4.2, "Model Components:", fontsize=8, fontweight='bold', fontfamily='serif')
ax.text(-4.5, -4.4, "• Nucleus: Central Hub", fontsize=6, fontfamily='serif')
ax.text(-4.5, -4.6, "• Sensory: Inputs", fontsize=6, fontfamily='serif')
ax.text(-4.5, -4.8, "• Cognitive: Processing", fontsize=6, fontfamily='serif')
ax.text(-4.5, -5.0, "• Physical: Responses", fontsize=6, fontfamily='serif')
ax.text(-4.5, -5.2, "• Resonance: Links", fontsize=6, fontfamily='serif')

plt.tight_layout() # Automatically adjust subplot params for a tight layout
plt.savefig("pram_network.png", dpi=300, bbox_inches='tight') # Save the figure in high resolution
plt.show() # Display the figure
