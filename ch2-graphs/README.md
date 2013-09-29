### Exercise 2 
*In this exercise you write methods that will be useful for many of the Graph algorithms that are coming up.*  

1. Download [thinkcomplex.com/GraphCode.py](http://thinkcomplex.com/GraphCode.py), which contains the code in this chapter. Run it as a script and make sure the test code in main does what you expect.  
2. Make a copy of `GraphCode.py` called `Graph.py`. Add the following methods to `Graph`, adding test code as you go.  
3. Write a method named `get_edge` that takes two vertices and returns the edge between them if it exists and None otherwise. Hint: use a try statement.  
4. Write a method named `remove_edge` that takes an edge and removes all references to it from the graph.  
5. Write a method named `vertices` that returns a list of the vertices in a graph.  
6. Write a method named `edges` that returns a list of edges in a graph. Note that in our representation of an undirected graph there are two references to each edge.  
7. Write a method named `out_vertices` that takes a Vertex and returns a list of the adjacent vertices (the ones connected to the given node by an edge).  
8. Write a method named `out_edges` that takes a Vertex and returns a list of edges connected to the given Vertex.  
9. Write a method named `add_all_edges` that starts with an edgeless Graph and makes a complete graph by adding edges between all pairs of vertices.  

Test your methods by writing test code and checking the output. Then download [thinkcomplex.com/GraphWorld.py](http://thinkcomplex.com/GraphWorld.py). GraphWorld is a simple tool for generating visual representations of graphs. It is based on the World class in Swampy, so you might have to install Swampy first: see [thinkpython.com/swampy](http://thinkpython.com/swampy).  

Read through GraphWorld.py to get a sense of how it works. Then run it. It should import your Graph.py and then display a complete graph with 10 vertices.