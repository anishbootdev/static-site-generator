from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    node = markdown_to_html_node(markdown)
    if node.children:
        for i in node.children:
            if i.tag == "h1":
                return i.value
    raise ValueError("No title found in markdown")