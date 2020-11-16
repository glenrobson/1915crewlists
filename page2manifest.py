#!/usr/bin/env python3

import sys
import requests
import string
import json
import re
import html as htmlformatter
from pathlib import Path
import os.path
from bs4 import BeautifulSoup
from bottle import template

def data2dict(section):
    headings = []
    for dt in section.dl.find_all('dt'):
        headings.append(dt.string.replace(':',''))

    index = 0
    data = {}
    for dd in section.dl.find_all('dd'):
        data[headings[index]] = string.capwords(dd.string.strip())
        index +=1

    return (headings, data)

def generateCanvases(html, fields):
    canvases = []
    for anchor in html.find_all("a", class_="document__link"):
        fields['image_url'] = "https://1915crewlists.rmg.co.uk{}".format(anchor['href'])
        fields['file_id'] = os.path.basename(anchor['href'])[:-4]
        size = anchor['data-size'].split("x")
        fields['width'] = size[0]
        fields['height'] = size[1]

        thumb = anchor.div.img
        fields['thumb_url'] = "https://1915crewlists.rmg.co.uk{}".format(thumb['data-src'])
        fields['thumb_width'] = int(240 / (int(size[1]) / int(size[0])) )
        fields['thumb_height'] = 240

        canvas = json.loads(template('templates/canvas.json', fields))
        canvases.append(canvas)

    return canvases

if __name__ == "__main__":
    if len(sys.argv) != 2:
        doc_id = 189083
        print ('Usage:\n\t{} [Document id e.g. 189083 from https://1915crewlists.rmg.co.uk/document/189083]'.format(sys.argv[0]))
    else:
        doc_id = sys.argv[1]
    
    outputFile = "docs/manifests/{}/{}.json"

    url = "https://1915crewlists.rmg.co.uk/document/{}".format(doc_id)
    page = requests.get(url)

    if page.status_code == 200:
        html = BeautifulSoup(page.content, 'html.parser')
        fields = { "doc_id": doc_id}

        officalNumberText = html.find("h2", class_="header-sub-title")
        fields['ship_id'] = officalNumberText.string.replace("Official number: ","")

        outputFile = outputFile.format(fields['ship_id'], doc_id)
 
        (headings, data) = data2dict(html.find("section", class_="section-content__meta"))

        fields['label'] = "{}, {}".format(htmlformatter.unescape(html.find("h1", class_="header-title").string), data['Valid dates for this crew list']) 

        m = re.search("'(.+?)'", fields['label'])
        if m:
            fields['ship'] = string.capwords(m.group(1))

        manifest = json.loads(template('templates/manifest.json', fields))
        for key in headings:
            manifest['metadata'].append(
                {
                  "label": { "en": [ key ] },
                  "value": { "en": [ data[key] ] }
                }
            )

        manifest['items'] = generateCanvases(html, fields)

        Path(os.path.dirname(outputFile)).mkdir(parents=True, exist_ok=True)
        with open(outputFile, 'w') as outfile:
            json.dump(manifest, outfile, indent=4)

    else:
        print('Failed to get URL: {} Got: {}'.format(url,page.status_code))


