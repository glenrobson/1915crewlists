## 1915 Crewlists data

A page to give access to machine readable data from the excellent:

https://1915crewlists.rmg.co.uk


### CSV files:

Generated CSV files:

<ul>
    {% for datafile in site.data.csv %}
    {% assign row = datafile[1] %}
      <li>
        <a href="https://github.com/glenrobson/1915crewlists/tree/main/docs/_data/csv/{{ datafile }}">
          {{ row.Vessel }}
        </a>
      </li>
    {% endfor %}
</ul>
