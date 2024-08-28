block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    markdown = markdown.lstrip("\n")
    lines = markdown.split("\n\n")
    lines = [line.strip() for line in lines]
    for line in lines[::-1]:
        if line == '':
            lines.pop()
        else:
            break
    blocks = []
    for line in lines:
        if line == "":
            continue
        splitlines = line.split("\n")
        splitlines = [line.strip() for line in splitlines]
        line = '\n'.join(splitlines)
        blocks.append(line)

    return blocks

def block_to_block(block):
    if block[0] == "#":
        return block_type_heading
    elif block.startswith("```") and block.endswith("```"):
        return block_type_code
    elif block[0:2] == "> ":
        if all(line[0] == ">" for line in block.split("\n")):
            return block_type_quote
    elif block[0:2] == "* " or block[0:2] == "- ":
        return block_type_ulist
    elif block[0:3] == "1. ":
        return block_type_olist
    else:
        return block_type_paragraph