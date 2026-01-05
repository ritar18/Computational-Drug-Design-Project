
#import necessary libraries
import os  #to allow file operations
import networkx as nx  #to convert to a graph and traverse it
import matplotlib.pyplot as plt  #to visualtize the graph


#ask the user to enter the directory path of the folder that contains the molecules
path = input("enter the directory path: ")

#get all filenames  from the path directory and store them in "files"
files = os.listdir(path)

#loop through files 
for file in files:
    #open and read each item in files after checking if it is a file and has a ".mol" extension
    if os.path.isfile(os.path.join(path, file)) and file.endswith(".mol"):
        with open(os.path.join(path, file), 'r') as f:
            #skip the first three lines in the file (since they are useless(header info))
            for i in range(3):
                f.readline()
            
            info_needed = f.readline() #reads the 4th line (after the 3 skipped lines)
            line=info_needed.split() #split the current line into a list 
            if(len(line))>2: #checking if the length of this list is greater than 2 (only the first two elements are needed)
                number_of_nodes = int(line[0]) #the first index tells us the number of atoms (nodes in our graph) 
                number_of_edges = int(line[1]) #the second index tells us the number of bonds (edges in our graph)

            #create two empty lists that will contain the x and y coordinates of each atom in the molecule
            x = []
            y = []

            #loop processes each line representing the coordinates of atoms (nodes) in the molecule and then split each line into a list
            for i in range(number_of_nodes):
                l2 = f.readline().split()
                if(len(l2))>2: #checking if the length of this list is greater than 2 (only the first two elements are needed)
                    #extracting the x and y coordinates
                    x.append(float(l2[0])) #append to list x the x-coordinates 
                    y.append(float(l2[1])) #append to list y the y-coordinates 


                
            #create an empty list that will contain source and targets for each  bond (edges)
            edges = []
            #loop processes each line representing the source and the target of each bond in the molecule and then split each line into a list
            for i in range(number_of_edges):
                l3 = f.readline().split()
                if(len(l3))>2: #checking if the length of this list is greater than 2 (only the first two elements are needed)
                    edges.append((int(l3[0]), int(l3[1]))) #append the source and the target of each bond
                    

        #create a graph (NetworkX) using the preceding lists
        G = nx.Graph()
        G.add_nodes_from(range(1, number_of_nodes + 1)) #assuming node indices start from 1
        G.add_edges_from(edges)


        #visualize the graph using matplotlib
        nx.draw(G, with_labels=True)
        plt.title(f"Graph for {file}")
        plt.show()

        #for each node in the graph, use NetworkX function to get its eccentricity
        eccentricities = nx.eccentricity(G)

        #find the largest (diameter) and smallest (radius) eccentricities
        diameter = max(eccentricities.values())
        radius = min(eccentricities.values())
        
        #calculate petit jean index 
        petitjean_index = (diameter- radius) / radius


        #for each file print its name and petit jean index
        print(f"For {file}:")
        print(f"Petitjean Index: {petitjean_index}")
