# Static Site Generator (SSG)

This is a simple static site generator that converts markdown files into HTML pages. It processes markdown content, applies a template, and generates HTML files to serve a static website.

## Features
- Recursively processes markdown files from the `content` directory.
- Converts markdown to HTML and inserts it into a template.
- Generates HTML files in the `public` directory.
- Automatically serves the site on `localhost:8888`.


### Directory Explanations

- **content/**: This is where you place your markdown files. You can organize them in subdirectories as needed.
- **public/**: This is the output directory where the generated HTML files will be stored. It is automatically created and updated by the script.
- **static/**: Any static assets such as images, stylesheets, or scripts go here. These files will be copied to the `public/` folder during generation.
- **template.html**: This is the HTML template used for all pages. `{{ Title }}` will be replaced with the page title from your markdown and `{{ Content }}` with the converted markdown content.

## How to Use

### 1. Place Your Content
Add your markdown files to the `content/` directory. These files can be nested in subdirectories if desired.

### 2. Run the Generator
To generate the static site, run the following command:

```bash
./main.sh
```
This will generate HTML files from your markdown content and copy them into the public/ directory.

### 3. Serve the site
After running the script, the site will automatically be served at http://localhost:8888.


### Notes
* You can refer to the content directory in the repository and the MD files inside it as an example.
* If there are errors during the generation process, check the console for file not found or other error messages.
