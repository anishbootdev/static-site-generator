from textnode import TextNode, TextType

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK_TEXT, url="https://example.com")
    print(text_node)

main()
