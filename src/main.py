from textnode import TextNode, TextType

def main():
	text_node_obj = TextNode("Hello world", TextType.BOLD, "https://google.com" )
	print(text_node_obj)

main()