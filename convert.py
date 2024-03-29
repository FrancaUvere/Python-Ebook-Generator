#!/usr/bin/env python3

import csv
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

html_file = 'template2.html'



def read_csv(file):
    data = []
    i = 0
    with open(file, 'r') as f:
        for row in f:
            i += 1
            author = row.split(",")[-1].replace('"', '')
            quote = row.split("-")[0].replace('"', '')
            data.append({'quote': quote, 'author': author} )


    return data
    
def generate_pdf(html_file):
    """This function generates the pdf"""
    # Read data from CSV file
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(html_file)

    # Render the template with the provided data
    rendered_html = template.render(data=read_csv('Creativity.csv'))

    # Configure PDF options (optional)

    # Generate PDF from HTML using WeasyPrint
    HTML(string=rendered_html).write_pdf('quotes_sample2.pdf', stylesheets=['styles.css'], presentational_hints=True)


    print('success')

generate_pdf(html_file)



