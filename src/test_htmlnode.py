import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
	def test_props_to_html(self):
		node = HTMLNode("div", "Hello, world!", props={"href": "https://www.google.com", "target": "_blank"})
		self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

	def test_html_node(self):
		node = HTMLNode("div", "Hello, world!")
		self.assertEqual(node.tag, "div")
		self.assertEqual(node.value, "Hello, world!")
		self.assertIsNone(node.children)
		self.assertIsNone(node.props)

	def test_html_node_repr(self):
		node = HTMLNode("div", "Hello, world!")
		self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, world!, children=None, props=None)")

	def test_to_html_no_children(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_to_html_no_tag(self):
		node = LeafNode(None, "Hello, world!")
		self.assertEqual(node.to_html(), "Hello, world!")

	def test_parent_no_children(self):
		node = ParentNode("div", None)
		with self.assertRaises(ValueError):
			node.to_html()

	def test_parent_no_tag(self):
		node = ParentNode(None, [LeafNode("p", "Hello, world!")])
		with self.assertRaises(ValueError):
			node.to_html()

	def test_parent(self):
		node = ParentNode("div", [LeafNode("p", "Hello, world!")])
		self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")

	def test_parent_2(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

	def test_parent_with_props(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
			props={"class": "paragraph"},
		)
		self.assertEqual(node.to_html(),
		                 '<p class="paragraph"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

	def test_parent_with_leaf_prop(self):
		node = ParentNode('div', [LeafNode('p', 'Hello, world!', props={'class': 'paragraph'})])
		self.assertEqual(node.to_html(), '<div><p class="paragraph">Hello, world!</p></div>')

	def test_parent_with_lef_pro_anchor(self):
		node = ParentNode('div', [LeafNode('a', 'Google', props={'href': 'https://www.google.com', 'target': '_blank'})])
		self.assertEqual(node.to_html(), '<div><a href="https://www.google.com" target="_blank">Google</a></div>')