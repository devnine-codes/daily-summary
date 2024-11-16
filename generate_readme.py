import os

def generate_summary(root_dir):
    output = "# daily-summary\n\n"
    for year in sorted(os.listdir(root_dir)):
        year_path = os.path.join(root_dir, year)
        if os.path.isdir(year_path) and year.isdigit():
            output += f"<details>\n<summary>📂 {year}</summary>\n\n"
            for month in sorted(os.listdir(year_path)):
                month_path = os.path.join(year_path, month)
                if os.path.isdir(month_path):
                    for subfolder in sorted(os.listdir(month_path)):
                        subfolder_path = os.path.join(month_path, subfolder)
                        if os.path.isdir(subfolder_path):
                            readme_path = os.path.join(subfolder_path, "README.md")
                            if os.path.exists(readme_path):
                                title = subfolder.replace("_", " ")
                                output += f"- [{title}]({year}/{month}/{subfolder}/README.md)\n"
            output += "\n</details>\n\n"
    return output

def main():
    root_dir = "."
    summary = generate_summary(root_dir)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(summary)

if __name__ == "__main__":
    main()
