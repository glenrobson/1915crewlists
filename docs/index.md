
A page to give access to machine readable data from the excellent:

[https://1915crewlists.rmg.co.uk](https://1915crewlists.rmg.co.uk)

The code to create the downloads is available here:

[https://github.com/glenrobson/1915crewlists/](https://github.com/glenrobson/1915crewlists/)

### CSV files:

Generated CSV files:

<ul>
    {% for datafile in site.data.csv %}
    {% assign row = datafile[0] %}
      <li>
        <a href="https://github.com/glenrobson/1915crewlists/tree/main/docs/_data/csv/{{ datafile[0] }}.csv">
          {{ datafile[0] }} - {{ datafile[1][0]["Vessel"] }}
        </a>
      </li>
    {% endfor %}
</ul>
