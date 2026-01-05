# Computational-Drug-Design-Project
This project was completed as part of the “Computational Drug Design” course during my Bachelor’s studies at the Lebanese American University. It focuses on analyzing molecular structures by calculating the Petitjean Index, a topological descriptor that captures the shape and branching of molecules. In other words, it measures how branched or elongated a molecule is; a low Petitjean index means that the molecule is compact while a high value means that the molecule is more branched. Each molecule is represented as a graph where atoms are nodes and bonds are edges. The Petitjean Index is computed using the molecule’s diameter (the longest shortest path between any two atoms) and radius (the shortest eccentricity among all atoms). This metric is very useful in cheminformatics and drug design, since molecular topology can influence properties such as reactivity, binding affinity, and pharmacokinetics.

The project also includes a visualization component, where molecules are displayed as graphs using NetworkX and matplotlib, allowing the user to explore molecular topology. 

Key Steps of the Code: 
- Data Input: User provides a folder containing .mol files (the molecules)
- Graph Construction: Each molecule is converted into a graph where nodes represent atoms and edges represent bonds.
- Visualization: Molecules are visualized as graphs.
- Petitjean Index Calculation:
1) Compute the eccentricity of each node (maximum distance to any other node).
2) Determine diameter (largest eccentricity) and radius (smallest eccentricity).
3) Calculate Petitjean Index = (diameter – radius) / radius.

Output: For each molecule, the Petitjean Index is displayed along with its graph.
