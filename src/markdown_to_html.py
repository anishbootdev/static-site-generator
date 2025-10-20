from htmlnode import HTMLNode,ParentNode, LeafNode
from inline_markdown import markdown_to_blocks
from block import block_to_block_type, BlockType
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes,markdown_to_blocks


def create_html_node_from_block(block, block_type):
    if block_type == BlockType.HEADING:
        level = len(block) - len(block.lstrip("#"))
        content = block.lstrip("#").strip()
        return LeafNode(f"h{level}", content, None)
    elif block_type == BlockType.PARAGRAPH:
        block_list = [b.strip() for b in block.split("\n")]
        block = ""
        for b in block_list:
            if b != "":
                block += b + " "
        block = block.strip()
        text_nodes = text_to_textnodes(block)
        html_children = [text_node_to_html_node(tn) for tn in text_nodes]
        return ParentNode("p", html_children, None)
    elif block_type == BlockType.CODE:
        lines = block.split("\n")
        inner = "\n".join(lines[1:-1])
        if inner and not inner.endswith("\n"):
            inner += "\n"
        return ParentNode("pre", [LeafNode("code", inner, None)], None)
    # python
    elif block_type == BlockType.QUOTE:
        # normalize: strip each '>' and join with spaces
        lines = block.split("\n")
        quote_text = " ".join(line.lstrip("> ").strip() for line in lines if line.strip() != "")
        # inline parse
        text_nodes = text_to_textnodes(quote_text)
        html_children = [text_node_to_html_node(tn) for tn in text_nodes]
        return ParentNode("blockquote", html_children, None)
    elif block_type == BlockType.UNORDERED_LIST:
        items = block.split("\n")
        li_children = []
        for item in items:
            item_content = item.lstrip("- ").strip()
            text_nodes = text_to_textnodes(item_content)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            li_children.append(ParentNode("li", html_children, None))
        return ParentNode("ul", li_children, None)
    elif block_type == BlockType.ORDERED_LIST:
        items = block.split("\n")
        li_children = []
        for item in items:
            item_content = item[3:].strip()
            text_nodes = text_to_textnodes(item_content)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            li_children.append(ParentNode("li", html_children, None))
        return ParentNode("ol", li_children, None)
    else:
        raise ValueError(f"Unsupported block type: {block_type}")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        try:
            html_node = create_html_node_from_block(block, block_type)
            children.append(html_node)
        except Exception as e:
            print(f"Error processing block: {e}")
    return ParentNode("div", children, None)
