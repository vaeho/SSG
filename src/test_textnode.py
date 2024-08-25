import unittest

from textnode import TextNode
from htmlnode import *
from main import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is also a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def text_to_html(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(text_node_to_html_node(node), LeafNode("This is a text node", "b"))

        node = TextNode("This is a link text", "link", "https://www.example.com")
        self.assertEqual(text_node_to_html_node(node), LeafNode("This is a link text", "a", {"href" : "https://www.example.com"}))

        node = TextNode("This is a code text", "code")
        self.assertEqual(text_node_to_html_node(node), LeafNode("This is a code text", "code"))

        node = TextNode("This is an image text", "image", "https://www.example.com/image.png")
        self.assertEqual(text_node_to_html_node(node), LeafNode('', "img", {"src" : "https://www.example.com/image.png", "alt" : "This is an image text"}))

        node = TextNode("This is text", "text")
        self.assertEqual(text_node_to_html_node(node), LeafNode("This is text", None))
        
        node = TextNode("This is italic text", "italic")
        self.assertEqual(text_node_to_html_node(node), LeafNode("This is italic text", "i"))


if __name__ == "__main__":
    unittest.main()