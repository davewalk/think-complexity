"""
Tests for Exercise 2 of the Think Complexity book
"""

import unittest
import Graph

class GraphTests(unittest.TestCase):

	def testGetEdgeReturnEdge(self):
		v = Graph.Vertex('v')
		w = Graph.Vertex('w')
		e = Graph.Edge(v, w)
		g = Graph.Graph([v,w], [e])
		self.assertIsInstance(g.get_edge(v, w), Graph.Edge)

	def testGetEdgeReturnsNone(self):
		v = Graph.Vertex('v')
		w = Graph.Vertex('w')
		x = Graph.Vertex('x')
		e = Graph.Edge(v, w)
		g = Graph.Graph([v,w], [e])
		self.assertIsNone(g.get_edge(v, x))	

if __name__ == '__main__':
	unittest.main(exit=False)

