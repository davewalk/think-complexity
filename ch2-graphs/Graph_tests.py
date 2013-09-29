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

	def testRemoveEdge(self):
		v = Graph.Vertex('v')
		w = Graph.Vertex('w')
		e = Graph.Edge(v, w)
		g = Graph.Graph([v,w], [e])
		g.remove_edge(e)
		self.assertIsNone(g.get_edge(v,w))

	def testVerticesMethod1(self):
		v = Graph.Vertex('v')
		w = Graph.Vertex('w')
		x = Graph.Vertex('x')
		e = Graph.Edge(v, w)
		g = Graph.Graph([v,w,x], [e])
		vertices = g.vertices()
		self.assertEqual(len(vertices), 3)

	def testVerticesMethod2(self):
		v = Graph.Vertex('v')
		w = Graph.Vertex('w')
		x = Graph.Vertex('x')
		e = Graph.Edge(v, w)
		g = Graph.Graph([v,w,x], [e])
		vertices = g.vertices()
		self.assertIsInstance(vertices[0], Graph.Vertex)

if __name__ == '__main__':
	unittest.main(exit=False)

