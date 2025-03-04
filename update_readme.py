from datetime import datetime

README_FILE = "README.md"

# 📆 Calcule le nombre de jours restants avant la nouvelle année
def get_days_until_new_year():
    today = datetime.today()
    next_year = datetime(today.year + 1, 1, 1)
    days_remaining = (next_year - today).days
    
    # Si le nombre de jours est égal à 1, utiliser "day" au lieu de "days"
    if days_remaining == 1:
        return f"**1 day before {next_year.year} ⏱**"
    else:
        return f"**{days_remaining} days before {next_year.year} ⏱**"
    
    # return f"**{days_remaining} days before {next_year.year} ⏱**"

# 📅 Récupère la date d'aujourd'hui
def get_today_date():
    return datetime.today().strftime("%A, %B %d, %Y")

# 🔄 Ajoute ou met à jour la section avec les nouvelles infos
def update_readme():
    try:
        with open(README_FILE, "r", encoding="utf-8") as file:
            content = file.read()

        # Texte à insérer dans le README
        custom_section = f"""
---

📅 **Today's Date:** {get_today_date()}  
⏳ **Countdown to New Year:** {get_days_until_new_year()}  

---
"""

        # Vérifier si la section existe déjà, sinon l'ajouter à la fin
        start_marker = "<!-- AUTO-UPDATE-SECTION -->"
        end_marker = "<!-- END-AUTO-UPDATE-SECTION -->"

        if start_marker in content and end_marker in content:
            # Remplacer l'ancienne section
            new_content = content.split(start_marker)[0] + start_marker + custom_section + end_marker + content.split(end_marker)[1]
        else:
            # Ajouter la section à la fin du README
            new_content = content.strip() + f"\n{start_marker}{custom_section}{end_marker}\n"

        with open(README_FILE, "w", encoding="utf-8") as file:
            file.write(new_content)

        print("✅ README.md mis à jour avec succès !")
    except FileNotFoundError:
        print(f"❌ Le fichier {README_FILE} n'existe pas.")

# 🚀 Exécute la mise à jour
if __name__ == "__main__":
    update_readme()
