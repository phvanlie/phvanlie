from datetime import datetime

README_FILE = "README.md"

# 📆 Calculates the number of days remaining until the new year
def get_days_until_new_year():
    today = datetime.today()
    next_year = datetime(today.year + 1, 1, 1)
    days_remaining = (next_year - today).days
    
    # If the number of days is equal to 1, use "day" instead of "days"
    if days_remaining == 1:
        return f"**1 day before {next_year.year} ⏱**"
    else:
        return f"**{days_remaining} days before {next_year.year} ⏱**"

# 📅 Retrieves today's date
def get_today_date():
    return datetime.today().strftime("%A, %B %d, %Y")

# 🔄 Adds or updates the section with new information
def update_readme():
    try:
        with open(README_FILE, "r", encoding="utf-8") as file:
            content = file.read()

        # Text to insert into the README
        custom_section = f"""

📅 **Today's Date:** {get_today_date()}  
⏳ **Countdown to New Year:** {get_days_until_new_year()}  

"""

        # Check if the section already exists, otherwise add it to the end
        start_marker = "<!-- AUTO-UPDATE-SECTION -->"
        end_marker = "<!-- END-AUTO-UPDATE-SECTION -->"

        if start_marker in content and end_marker in content:
            # Replace the old section
            new_content = content.split(start_marker)[0] + start_marker + custom_section + end_marker + content.split(end_marker)[1]
        else:
            # Add the section to the end of the README
            new_content = content.strip() + f"\n{start_marker}{custom_section}{end_marker}\n"

        with open(README_FILE, "w", encoding="utf-8") as file:
            file.write(new_content)

        print("✅ README.md updated successfully!")
    except FileNotFoundError:
        print(f"❌ The file {README_FILE} does not exist.")

# 🚀 Executes the update
if __name__ == "__main__":
    update_readme()
