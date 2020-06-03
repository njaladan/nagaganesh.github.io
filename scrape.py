from os import listdir
from os.path import isfile, join
from datetime import datetime


base = """---
layout: post
title:  "{0}"
tags: [ Books ]
link: {1}
---

"""

mypath = "./books/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles[0])

book = onlyfiles[0]

for book in onlyfiles:
    with open(mypath + book) as f:
        book_parts = book.lower().split(" ")
        new_title = "-".join(book_parts[:-1])
        title = f.readline()
        f.readline()
        date = f.readline().split(":")[1].strip()
        genre = f.readline()
        publish = f.readline()
        f.readline()
        content = f.read()
        newdate = datetime.strptime(date, "%b %d, %Y").strftime("%Y-%m-%d")
        filename = f"{newdate}-{new_title}.md"
        with open("./parsebooks/" + filename, "w+") as new_f:
            full_title = title[2:].strip()
            new_f.write(base.format(full_title, "true" if publish == "Yes" else "false"))
            new_f.write(content)
    