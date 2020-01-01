import datetime
import unidecode
import os

date = datetime.date.today().strftime("%Y-%m-%d")

print("Welcome to MEZIKLASI article markdown template generator")

name = ""
while len(name.split()) == 0:
	name = input("Article title: ")
category = ""
while len(category.split()) == 0:
	category = input("Article category: ")

description = input("Article RSS description (optional): ")
print("generating...")

header = f"""---
layout: post
title: "{name}"
date: {date}
category: {category}
description: "{description if len(description.split()) > 0 else ""}"
---


"""

draft_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "..",
    "_drafts",
    f"{date}-{unidecode.unidecode(name.replace(' ', '-'))}.md",
)

with open(draft_path, "w") as file:
    file.write(header)

print("Done")
os.system(f"vim {draft_path}")
