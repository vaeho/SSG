import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode(tag="a", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(repr(node), "HTMLNode(a, None, None, {'href': 'https://www.example.com', 'target': '_blank'})")

    def test_none(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.example.com" target="_blank"')


class TestParentNode(unittest.TestCase):
    def test_init(self):
        node = ParentNode("div", [LeafNode("This is a leaf node", "p", {"class": "bold"}), LeafNode("This is another leaf node", "b"), LeafNode("This is yet another leaf node")], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, [LeafNode("This is a leaf node", "p", {"class": "bold"}), LeafNode("This is another leaf node", "b"), LeafNode("This is yet another leaf node")])
        self.assertEqual(node.props, {"class": "container"})
        node2 = ParentNode("span", [LeafNode("Leaf Node")])
        self.assertEqual(node2.children, [LeafNode("Leaf Node")])
        self.assertEqual(node2.props, None)
        self.assertEqual(node2.tag, "span")
    
    def test_to_html(self):
        node = ParentNode("div", [LeafNode("This is a leaf node", "p", {"class": "bold"}), LeafNode("This is another leaf node", "b"), LeafNode("This is yet another leaf node")], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p class="bold">This is a leaf node</p><b>This is another leaf node</b>This is yet another leaf node</div>')

        node1 = ParentNode("span", [LeafNode("Leaf Node")])
        self.assertEqual(node1.to_html(), '<span>Leaf Node</span>')
        
        node2 = ParentNode("div", None)
        self.assertRaises(ValueError, node2.to_html)

        node3 = ParentNode(None, [LeafNode("Leaf Node")])
        self.assertRaises(ValueError, node3.to_html)
    
    def test_repr(self):
        self.maxDiff = None
        node = ParentNode("div", [LeafNode("This is a leaf node", "p", {"class": "bold"}), LeafNode("This is another leaf node", "b"), LeafNode("This is yet another leaf node")], {"class": "container"})
        self.assertEqual(repr(node), "ParentNode(div, [LeafNode(This is a leaf node, p, {'class': 'bold'}), LeafNode(This is another leaf node, b, None), LeafNode(This is yet another leaf node, None, None)], {'class': 'container'})")
        node2 = ParentNode("span", [LeafNode("Leaf Node")])
        self.assertEqual(repr(node2), "ParentNode(span, [LeafNode(Leaf Node, None, None)], None)")
    

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode("This is a leaf node")
        self.assertEqual(node.value, "This is a leaf node")
        self.assertEqual(node.tag, None)
        self.assertEqual(node.props, None)
        self.assertEqual(repr(node), "LeafNode(This is a leaf node, None, None)")
    
    def test_to_html(self):
        node = LeafNode("This is a leaf node")
        self.assertEqual(node.to_html(), "This is a leaf node")
        node = LeafNode("This is a leaf node", "p", {"class": "bold"})
        self.assertEqual(node.to_html(), '<p class="bold">This is a leaf node</p>')

    def test_value_none(self):
        node = LeafNode(None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()