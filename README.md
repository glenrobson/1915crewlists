# 1915crewlists
Download data as a CSV from https://1915crewlists.rmg.co.uk e.g. https://1915crewlists.rmg.co.uk/document/189083


## Building:

Requires python3 and the following libraries: 

```
pip3 install -r requirements.txt 
```

## scripts

Usage:
	python3 page2csv.py [Document id e.g. 189083 from https://1915crewlists.rmg.co.uk/document/189083] [optional output file]

Where `doc_id` is the last number in the 1915 Crew lists site e.g.:

 * [https://1915crewlists.rmg.co.uk/document/189083](https://1915crewlists.rmg.co.uk/document/189083)

By default the output file is `data/doc_id.csv` but you can provide a parameter to specify a different directory 
