#!/usr/bin/env python3

import sys
import requests
import string
import csv
from bs4 import BeautifulSoup

if __name__ == "__main__":
    datafile = 'data/{}.csv'
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        doc_id = 189083
        print ('Usage:\n\t{} [Document id e.g. 189083 from https://1915crewlists.rmg.co.uk/document/189083] [optional output file]'.format(sys.argv[0]))
        print ('Using default: {} {}'.format(doc_id, datafile.format(doc_id)))
        datafile = datafile.format(doc_id)
    else:
        doc_id = sys.argv[1]
        if sys.argv > 2:
            datafile = sys.argv[2]
        else:
            datafile = datafile.format(doc_id)

    url = "https://1915crewlists.rmg.co.uk/document/{}".format(doc_id)
    page = requests.get(url)

    if page.status_code == 200:
        html = BeautifulSoup(page.content, 'html.parser')

        ship = []
        records = html.find_all("div", class_="record")
        rows = []
        headings = []
        for dt in records[0].div.dl.find_all('dt'):
            headings.append(dt.string.replace(':','').lower())

        for record in records:
            name = string.capwords(record.h3.string)

            data = {
                'name': name
            }
            index = 0
            for dd in record.div.dl.find_all('dd'):
                data[headings[index]] = string.capwords(dd.string.strip())
                index +=1

            if data['vessel'] not in ship:
                ship.append(data['vessel'])

            rows.append(data)

        headings.insert(0, "name")    

        with open(datafile, 'w', newline='') as csvfile:
            output = csv.writer(csvfile)
            row = []
            for heading in headings:
                row.append(string.capwords(heading))
            output.writerow(row)
            for data in rows:
                row = []
                for key in headings:
                    row.append(data[key])
                output.writerow(row)    

            print ('Saving output to {}'.format(datafile))
                
    else:
        print('Failed to get URL: {} Got: {}'.format(url,page.status_code))
