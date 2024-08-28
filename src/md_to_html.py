# from mdblocks import *
# from htmlnode import *


# def heading_block_to_html(block):
#     lines = block.split("\n")
#     nodes = []
#     for line in lines:
#         if line.startswith("######"):
#             nodes.append(LeafNode(tag="h6", value=line[6:]))
#         elif line.startswith("#####"):
#             nodes.append(LeafNode(tag="h5", value=line[5:]))
#         elif line.startswith("####"):
#             nodes.append(LeafNode(tag="h4", value=line[4:]))
#         elif line.startswith("###"):
#             nodes.append(LeafNode(tag="h3", value=line[3:]))
#         elif line.startswith("##"):
#             nodes.append(LeafNode(tag="h2", value=line[2:]))
#         elif line.startswith("#"):
#             nodes.append(LeafNode(tag="h1", value=line[1:]))
    
#     return nodes




# def markdown_to_html_node(markdown):
#     blocks = markdown_to_blocks(markdown)
#     htmlnodes = []
#     for block in blocks:
#         if block_to_block(block) == block_type_heading:
#             htmlnodes.extend(heading_block_to_html(block))
#         elif block_to_block(block) == block_type_code:
#             htmlnodes.append(ParentNode("pre", children=[LeafNode(tag="code", value=block[4:-3])]))
#         elif block_to_block(block) == block_type_quote:
#             htmlnodes.append(LeafNode(tag="blockquote", value=''.join(block.split("> "))))
#         elif block_to_block(block) == block_type_ulist:
#             listitems = block.split("\n")
#             children = [LeafNode(item[2:], "li") for item in listitems]
#             htmlnodes.append(ParentNode("ul", children))
#         elif block_to_block(block) == block_type_olist:
#             listitems = block.split("\n")
#             listitems = [item[item.find(" ")+1:] for item in listitems]
#             children = [LeafNode(item, "li") for item in listitems]
#             htmlnodes.append(ParentNode("ol", children))
#         else:
#             htmlnodes.append(LeafNode(block, "p"))

#     return ParentNode("div", htmlnodes)