import datetime
import unidecode
import os

date = datetime.date.today().strftime("%Y-%m-%d")

print("Welcome to MEZIKLASI article markdown template generator")

name = input("Article title: ")
category = input("Article category: ")
print("generating...")

header = f"""---
layout: post
tittle: "{name}"
date: {date}
category: {category}
---


"""

drafts_folder = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "..",
    "_drafts",
    f"{date}-{unidecode.unidecode(name.replace(' ', '-'))}.md",
)

with open(drafts_folder, "w") as file:
    file.write(header)

print("Done")
