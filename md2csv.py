import sys
import csv
from pathlib import Path

if(len(sys.argv) == 1):
    print('Run python ./md2csv.py $(find . -type f -name "*.md")')
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
                FAQ.append({"Q": q, "A": line[:-1]})
            questions = []
    return FAQ

# Get files
to_convert = sys.argv[1:]

# Conversion loop
for md_file in to_convert:
    faq_list = to_faq_list(md_file)
    outfile = f'./csv-knowledge/{Path(md_file).stem}.csv'
    with open(outfile, "w") as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=["Q", "A"])
        for faq in faq_list:
            writer.writerow(faq)