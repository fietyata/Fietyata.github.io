import scholarly
import os

def fetch_publications():
    search_query = scholarly.search_author('Your Name')
    author = next(search_query)
    scholarly.fill(author, sections=['publications'])

    publications = author['publications']
    publications_list = []

    for pub in publications:
        title = pub['bib']['title']
        authors = pub['bib'].get('author', 'N/A')
        year = pub['bib'].get('pub_year', 'N/A')
        publication = f"{title} - {authors} ({year})"
        publications_list.append(publication)
    
    return publications_list

def update_readme(publications):
    readme_path = "README.md"

    with open(readme_path, "r") as file:
        readme_content = file.readlines()

    start_marker = "<!-- PUBLICATIONS_START -->"
    end_marker = "<!-- PUBLICATIONS_END -->"
    start_idx = readme_content.index(start_marker + "\n")
    end_idx = readme_content.index(end_marker + "\n")

    new_content = readme_content[:start_idx+1] + \
                  ["\n".join(publications) + "\n"] + \
                  readme_content[end_idx:]

    with open(readme_path, "w") as file:
        file.writelines(new_content)

if __name__ == "__main__":
    publications = fetch_publications()
    update_readme(publications)
