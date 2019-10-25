import datetime

clean_dict = {"á": "a",
              "č": "c",
              "ď": "d",
              "é": "e",
              "ě": "e",
              "í": "i",
              "ň": "n",
              "ó": "o",
              "ř": "r",
              "š": "s",
              "ť": "t",
              "ý": "y",
              "ž": "z",
              " ": "-"}
date = datetime.date.today().strftime("%Y-%m-%d")


def make_file_name(text):
    text = text.lower()
    for i in range(len(text)):
        if text[i] in clean_dict.keys():
            text = text[:i] + clean_dict[text[i]] + text[i + 1:]
    text = date + "-" + text + ".md"
    return text


print("Welcome to MEZIKLASI article template generator")
name = input("Article tittle: ")
category = input("Article category: ")
header = '---\nlayout: post\ntittle: "' + name + '"\ndate: ' + date + '\ncategory: ' + category + '\n---\n\n\n'

file = open("../_drafts/" + make_file_name(name), "w")
file.write(header)
file.close() 
