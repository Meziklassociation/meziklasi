import datetime
import unidecode
import os

date = datetime.date.today().strftime("%Y-%m-%d")

print("Welcome to MEZIKLASI article markdown template generator")

name = input("Article title: ")
category = input("Article category: ")

header = f"""---
layout: post
title: "{name}"
date: {date}
category: {category}
---


"""

drafts_folder = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "..",
    "_drafts",
    f"{date}-{unidecode.unidecode(name.replace(' ', '-'))}",
)

with open(drafts_folder, "w") as file:
    file.write(header)
