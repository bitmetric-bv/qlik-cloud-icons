import os

# Get list of SVGs
items = os.listdir('./svg')
sorted_items = sorted(items)

# Initialize README.md
f = open("README.md", "w")
f.write("# Qlik Cloud icons\nCollection of " + str(len(sorted_items)) + " Qlik Cloud icons in SVG format.\n\n")

# Header
f.write("|Filename|Preview|\n|---|---|\n")

# Loop & write rows
for item in sorted_items:
    f.write("|" + item + "|<img src='./svg/" + item + "' width='32' height='32'/>|\n")

# Done
f.close()