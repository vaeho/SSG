from textnode import TextNode
from mdblocks import markdown_to_html_node, extract_title
from htmlnode import HTMLNode, ParentNode, LeafNode
import os
import shutil


def source_to_destination(source, destination):
    if os.path.isdir(source):
        os.mkdir(destination)
    items = os.listdir(source)
    for item in items:
        if os.path.isdir(os.path.join(f"{source}/{item}")):
            source_to_destination(os.path.join(f"{source}/{item}"), os.path.join(f"{destination}/{item}"))
        else:
            shutil.copy(os.path.join(f"{source}/{item}"), os.path.join(destination))

def generate_pages_recursive(from_path, template_path, dest_path):
    
    if os.path.isdir(from_path):
        srcdir = os.listdir(from_path)
        if not os.path.exists(dest_path):
            print(f"Creating directory {from_path} to {dest_path}")
            os.makedirs(dest_path)

        for item in srcdir:
            generate_pages_recursive(os.path.join(f"{from_path}/{item}"), template_path, os.path.join(f"{dest_path}/{item}"))
        return
    else:

        try:
            if os.path.isdir(dest_path):
                
                dest_path = os.path.join(dest_path, os.path.basename(from_path))

            print(f"Generating a page from {from_path} to {dest_path[:-3]}.html using {template_path}")
            with open(from_path, "r") as markdown_file:
                markdown = markdown_file.read()
            
            with open(template_path, "r") as template_file:
                template = template_file.read()

            html = markdown_to_html_node(markdown).to_html()
            
            title = extract_title(markdown)

            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html)

            dest_dir = os.path.dirname(f"{dest_path[:-3]}.html")
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            with open(f"{dest_path[:-3]}.html", "w") as dest_file:
                dest_file.write(template)

        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():

    public = "./public"
    static = "./static"
    content = "./content"
    template = "./template.html"

    if os.path.exists(public):
        shutil.rmtree(public)

    source_to_destination(static, public)
    
    generate_pages_recursive(content, template, public)


main()


