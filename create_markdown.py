import json
import os

def create_markdown_files(json_file_path, output_folder):
    # Load the JSON data
    # need to import individual json files
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # For each topic in the JSON
    for topic, search_terms in data.items():
        for search_term, urls in search_terms.items():
            for url, page_info in urls.items():

                # Create a new markdown file
                filename = f"article_{topic}_{page_info['title']}_{search_term}_{page_info['page search terms'][0]}.md"
                filepath = os.path.join(output_folder, filename)

                with open(filepath, 'w') as f:
                    # Write the markdown content
                    f.write(f"# {topic}\n\n")
                    f.write(f"## {page_info['title']}\n\n")
                    for snippet in page_info['page_text_snippets']:
                        f.write(f"{snippet}\n\n")
                    for image in page_info['image_links']:
                        f.write(f"![Image]({image})\n\n")
                    f.write(f"[Source]({url})")

# Usage
create_markdown_files('input.json', 'article')
