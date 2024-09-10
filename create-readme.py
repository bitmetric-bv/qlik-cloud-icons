import os

# Initialize README.md
f = open("README.md", "w")
f.write("# qlik-cloud-icons\nCollection of Qlik Cloud icons in SVG format\n\n|Filename|Preview|\n|---|---|\n")

# Get list of SVGs
items = os.listdir('./svg')
sorted_items = sorted(items)

# Loop & write
for item in sorted_items:
    f.write("|" + item + "|<img src='./svg/" + item + "' width='64' height='64'/>|\n")

# Done
f.close()