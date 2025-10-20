from textnode import TextNode, TextType
import os
import shutil

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
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    copy_folder("static", "public")
    print(node)


main()
