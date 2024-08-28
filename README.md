# Static Site Generator (SSG)

This is a simple static site generator that converts markdown files into HTML pages. It processes markdown content, applies a template, and generates HTML files to serve a static website.

## Features
- Recursively processes markdown files from the `content` directory.
- Applies a template to the markdown content.
- Copies static assets from the `static` directory.
- Generates HTML files in the `public` directory.
- Automatically serves the site on `localhost:8888`.


### Directory Explanations

- **content/**: This is where you place your markdown files. You can organize them in subdirectories as needed.
- **public/**: This is the output directory where the generated HTML files will be stored. It is automatically created and updated by the script.
- **static/**: Any static assets such as images, stylesheets, or scripts go here. These files will be copied to the `public/` folder during generation.
- **template.html**: This is the HTML template used for all pages. Use `{{ Title }}` to place the page title and `{{ Content }}` to insert the converted markdown content.

## How to Use

### 1. Place Your Content
Add your markdown files to the `content/` directory. These files can be nested in subdirectories if desired.

### 2. Customize the Template
Edit the `template.html` file to customize your site's layout. Make sure it contains the following placeholders:
- `{{ Title }}`: This will be replaced by the title extracted from your markdown file.
- `{{ Content }}`: This will be replaced by the generated HTML content.

### 3. Run the Generator
To generate the static site, run the following command:

```bash
./main.sh
```
This will generate HTML files from your markdown content and copy them into the public/ directory.

### 4. Serve the site
After running the script, the site will automatically be served at http://localhost:8888.


### Notes
* You can refer to the content directory in the repository and the MD files inside it as an example.
* If there are errors during the generation process, check the console for file not found or other error messages.
