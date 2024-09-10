import os


# Initialize README.md
f = open("README.md", "w")
f.write("# qlik-cloud-icons\nCollection of Qlik Cloud icons in SVG format\n\n|Filename|Preview|\n|---|---|\n")

# Get list of SVGs
items = os.listdir('./svg')
sorted_items = sorted(items)

# Loop & write
for item in sorted_items:
    svg = open("./svg/" + item, "r")
    f.write("|" + item + "|" + svg.read() + "|\n")
    svg.close()



# Done
f.close()