import re

START_TAG = "<!-- START_BLACKLIST_DEREXXD -->"
END_TAG = "<!-- END_BLACKLIST_DEREXXD -->"

# note - ai coded quick script over here
def update_readme():
    with open("blacklist.txt", "r", encoding="utf-8") as f:
        blacklist_content = f.read().strip()

    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()

    replacement = f"{START_TAG}\n```\n{blacklist_content}\n```\n{END_TAG}"

    pattern = re.compile(rf"{re.escape(START_TAG)}.*?{re.escape(END_TAG)}", re.DOTALL)
    new_readme_content = pattern.sub(replacement, readme_content)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme_content)

if __name__ == "__main__":
    update_readme()
