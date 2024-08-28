from mdblocks import *
import unittest

class TestMdblocks(unittest.TestCase):

    def test_markdown_to_blocks_headings(self):
            markdown = """
            # Heading 1
            ## Heading 2
            ### Heading 3
            #### Heading 4
            ##### Heading 5
            ###### Heading 6
            """
            self.assertListEqual(
                [
                    "# Heading 1\n## Heading 2\n### Heading 3\n#### Heading 4\n##### Heading 5\n###### Heading 6",
                ],
                markdown_to_blocks(markdown),
            )


    def test_markdown_to_blocks_multiblocks(self):
        markdown = """
        # Heading 1

        ## Heading 2

        * List item 1
        * List item 2

        
        Paragraph test


        """
        self.assertListEqual(
            [
                "# Heading 1",
                "## Heading 2",
                "* List item 1\n* List item 2",
                "Paragraph test",
            ],
            markdown_to_blocks(markdown),
        )


    def test_markdown_to_blocks_empty(self):
        markdown = ""
        self.assertListEqual(
            [],
            markdown_to_blocks(markdown),
        )

    def test_markdown_to_blocks_excessive_newlines(self):
        markdown = '''
        # Heading 1






        Paragraph test
        '''
        self.assertListEqual(
            [
                "# Heading 1",
                "Paragraph test",
            ],
            markdown_to_blocks(markdown),
        )

    def test_markdown_to_blocks_bd1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_block_to_block_heading(self):
        block = "# Heading 1"
        self.assertEqual("heading", block_to_block(block))
    
    def test_block_to_block_code(self):
        block = "```\ncode block\n```"
        self.assertEqual("code", block_to_block(block))
    
    def test_block_to_block_quote(self):
        block = "> This is a quote"
        self.assertEqual("quote", block_to_block(block))
    
    def test_block_to_block_quote_multiline(self):
        block = "> This is a quote\n> on multiple lines"
        self.assertEqual("quote", block_to_block(block))
    
    def test_block_to_block_unordered_list(self):
        block = "* List item 1\n* List item 2"
        self.assertEqual("unordered_list", block_to_block(block))
    
    def test_block_to_block_ordered_list(self):
        block = "1. List item 1\n2. List item 2"
        self.assertEqual("ordered_list", block_to_block(block))
    
    def test_block_to_block_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual("paragraph", block_to_block(block))

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()
