class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise Exception("NotImplementedError")

	def props_to_html(self):
		if self.props is None:
			return ""
		return " " + " ".join([f'{k}="{v}"' for k, v in self.props.items()])

	def __repr__(self):
		return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("Invalid HTML: no value")
		if self.tag is None:
			return self.value
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag is None:
			raise ValueError("Invalid HTML: no tag")

		if self.children is None:
			raise ValueError("Invalid HTML: no children")

		children_html ="".join([child.to_html() for child in self.children])
		return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

	def __repr__(self):
		return f"ParentNode({self.tag}, {self.children}, {self.props})"