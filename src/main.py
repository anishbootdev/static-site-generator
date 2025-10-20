from textnode import TextNode, TextType
import os
import shutil
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print("Generating page from ", from_path, " to ", dest_path, "using ", template_path)
    f = open(from_path, "r")
    markdown = f.read()
    f.close()
    f = open(template_path, "r")
    template = f.read()
    f.close()
    html_content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace("{{ Title }}", title)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    f = open(dest_path, "w")
    f.write(template)
        


def copy_folder(static, public):
    if os.path.exists(public):
        shutil.rmtree(public)
    os.makedirs(public)
    dirs = os.listdir(static)
    for d in dirs:
        if os.path.isfile(os.path.join(static, d)):
            shutil.copy(os.path.join(static, d), os.path.join(public, d))
        else:
            copy_folder(os.path.join(static, d), os.path.join(public, d))
            
def main():
    copy_folder("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


main()
