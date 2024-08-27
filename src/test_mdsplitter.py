import unittest
from mdsplitter import *

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )


    def test_extract_markdown_images(self):
        text = "![Image 1](/img/image1.png)![Image 2](/img/image2.png)"
        self.assertListEqual(
            [("Image 1", "/img/image1.png"), ("Image 2", "/img/image2.png")],
            extract_markdown_images(text),
        )

    def test_extract_markdown_links(self):
        text = "[Link 1](/link1)[Link 2](/link2)"
        self.assertListEqual(
            [("Link 1", "/link1"), ("Link 2", "/link2")],
            extract_markdown_links(text),
        )


    def test_split_nodes_image(self):
        node = TextNode("This is text with ![an image](/img/image.png)", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with ", text_type_text),
                TextNode("an image", text_type_image, "/img/image.png"),
            ],
            new_nodes,
        )

    def test_split_nodes_image_multiple(self):
        node = TextNode("This is text with ![an image](/img/image.png) and ![another image](/img/another_image.png)", text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with ", text_type_text),
                TextNode("an image", text_type_image, "/img/image.png"),
                TextNode(" and ", text_type_text),
                TextNode("another image", text_type_image, "/img/another_image.png"),
            ],
            new_nodes,
        )


    def test_split_nodes_link(self):
        node = TextNode("This is text with [a link](/link)", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with ", text_type_text),
                TextNode("a link", text_type_link, "/link"),
            ],
            new_nodes,
        )

    def test_split_nodes_link_multiple(self):
        node = TextNode("This is text with [a link](/link) and [another link](/another_link)", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with ", text_type_text),
                TextNode("a link", text_type_link, "/link"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "/another_link"),
            ],
            new_nodes,
        )

        def test_text_to_textnodes(self):
            nodes = text_to_textnodes(
                "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
            )
            self.assertListEqual(
                [
                    TextNode("This is ", text_type_text),
                    TextNode("text", text_type_bold),
                    TextNode(" with an ", text_type_text),
                    TextNode("italic", text_type_italic),
                    TextNode(" word and a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" and an ", text_type_text),
                    TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and a ", text_type_text),
                    TextNode("link", text_type_link, "https://boot.dev"),
                ],
                nodes,
            )

if __name__ == "__main__":
    unittest.main()
