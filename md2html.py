import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("./"))
template = env.get_template('template.html')

if(len(sys.argv) == 1):
    print('Run python ./md2html.py $(find . -type f -name "*.md")')
    exit()

# Conversion method
def to_faq_list(md_file) -> dict:
    FAQ = []
    questions = []
    for line in open(md_file, "r"):
        if line.startswith("###"):
            questions.append(line[3:-1])
        else:
            for q in questions:
                FAQ.append({"question": q, "answer": line[:-1]})
            questions = []
    return FAQ

# Get files
to_convert = sys.argv[1:]

# Conversion loop
for md_file in to_convert:
    faq_html = template.render(faq=to_faq_list(md_file))
    outfile = f'./html-knowledge/{Path(md_file).stem}.html'

    with open(outfile, "w") as out:
        out.write(faq_html)
