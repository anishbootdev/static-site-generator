from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_link

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        for alt_text, url in images:
            text = "![" + alt_text + "](" + url + ")"
            index = old_node.text.find(text)
            if index > 0:
                new_nodes.append(
                    TextNode(old_node.text[:index], TextType.TEXT, old_node.url)
                )
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            old_node.text = old_node.text[index + len(text) :]
        if old_node.text:
            new_nodes.append(TextNode(old_node.text, TextType.TEXT, old_node.url))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_link(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        for alt_text, url in links:
            text = "[" + alt_text + "](" + url + ")"
            index = old_node.text.find(text)
            if index > 0:
                new_nodes.append(
                    TextNode(old_node.text[:index], TextType.TEXT, old_node.url)
                )
            new_nodes.append(TextNode(alt_text, TextType.LINK, url))
            old_node.text = old_node.text[index + len(text) :]
        if old_node.text:
            new_nodes.append(TextNode(old_node.text, TextType.TEXT, old_node.url))
    return new_nodes

