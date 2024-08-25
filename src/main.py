from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(text_node.text, "b") # LeafNode(text_node.text, "b", {"href" : text_node.url}) if text_node.url else 
    elif text_node.text_type == "italic":
        return LeafNode(text_node.text, "i")
    elif text_node.text_type == "link":
        return LeafNode(text_node.text, "a", {"href" : text_node.url})
    elif text_node.text_type == "code":
        return LeafNode(text_node.text, "code") 
    elif text_node.text_type == "image":
        return LeafNode('', "img", {"src" : text_node.url, "alt" : text_node.text})
    else:
        raise Exception("Incorrect text type")

def main():
    text_node = TextNode("test text", "test type", "test url")
    print(text_node)
    
    

main()