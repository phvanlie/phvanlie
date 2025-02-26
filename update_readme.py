import os
import datetime

# Liste des citations dans l'ordre
citations = [
    "12345.",
    "La deuxième citation.",
    "La troisième citation.",
    "Et ainsi de suite..."
]

# Sélection de la citation du jour
index = datetime.date.today().toordinal() % len(citations)
citation_du_jour = citations[index]

# Lire le README actuel
with open("README.md", "r", encoding="utf-8") as f:
    content = f.readlines()

# Identifier et remplacer la ligne avec la citation
with open("README.md", "w", encoding="utf-8") as f:
    inside_block = False
    for line in content:
        if "<!-- CITE_START -->" in line:
            f.write("<!-- CITE_START -->\n")
            f.write(f"> **{citation_du_jour}**\n")
            inside_block = True
        elif "<!-- CITE_END -->" in line:
            f.write("<!-- CITE_END -->\n")
            inside_block = False
        elif not inside_block:
            f.write(line)

