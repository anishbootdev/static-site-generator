from textnode import TextNode, TextType
import os
import shutil
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
import sys

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dirs = os.listdir(dir_path_content)
    for d in dirs:
        if os.path.isfile(os.path.join(dir_path_content, d)):
            if d.endswith(".md"):
                from_path = os.path.join(dir_path_content, d)
                dest_path = os.path.join(dest_dir_path, d[:-3] + ".html")
                generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(os.path.join(dir_path_content, d), template_path, os.path.join(dest_dir_path, d), basepath)


def generate_page(from_path, template_path, dest_path, basepath):
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
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
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
    basepath = ""
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_folder("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
