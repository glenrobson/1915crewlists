
This is a page to demonstration the export of datasets from the [1915crewlists.rmg.co.uk](https://1915crewlists.rmg.co.uk) site. The source scripts to generate the CSV files and manifests are available on [GitHub](https://github.com/glenrobson/1915crewlists/).

The 1915 crew lists site gives access to lists of crew members who signed on and off ships during 1914 and 1915. These crew lists are a very valuable source of data to trace people and how they moved from ship to ship. Crew lists exist for all ships since 1835 but are split in various repositories. For more information on Crew lists see the [National Maritime Museum](https://www.rmg.co.uk/discover/researchers/research-guides/research-guide-c1-merchant-navy-tracing-people-crew-lists) research guide.

# Backstory

Through various reasons I've got very interested in a ship called the Canganian after finding it mentioned in the WW1 [Welsh Book of Remembrance](http://hdl.handle.net/10107/4642022). The Canganian was a steam powered coal transporter which sunk off the coast of Scotland after hitting a mine left by a U-Boat. I'm particularly interested in finding the non-Welsh crew which are missing from the Book of Remembrance. 

# Data

I've generated some data for the ship Canganian below partly to demonstrate the extract functions but also so I can investigate the data. Add an [issue](https://github.com/glenrobson/1915crewlists/issues) if you are struggling to generate a page and would like me to add it to this list.

## CSV files:

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


## Manifest files:

<ul>
{% for file in site.static_files %}
    {% if file.path contains 'manifests' %}
<li data-url="{{file.path | relative_url}}" class="manifest"><a href="{{ file.path }}">Manifest</a><ul><li>View in: <a href="https://projectmirador.org/embed/?iiif-content={{site.url}}{{site.baseurl}}{{ file.path }}">Mirador</a></li><li>View in: <a href="https://uv-v3.netlify.app/#?c=&m=&s=&cv=&manifest={{site.url}}{site.baseurl}}{{ file.path }}">UniversalViewer</a></li></ul></li>
    {% endif %}
{% endfor %}
</ul>

<script>
    var manifests = document.getElementsByClassName("manifest")
    var requests = [];
    for (var i = 0; i < manifests.length; i++) {
        var li = manifests[i];
        var xhr = new XMLHttpRequest();
        xhr.open("GET", li.dataset.url, false);
        xhr.onreadystatechange = function(){
            if (xhr.readyState === 4){
                if (xhr.status === 200){
                    console.log("xhr done successfully: " + li.dataset.url);
                    var manifest = JSON.parse(xhr.responseText);

                    li.firstChild.innerHTML = manifest.label.en[0];
                } else {
                    console.log("xhr failed");
                }
            } else {
                console.log("xhr processing going on " + li.dataset.url);
            }
        }
        xhr.send();
        requests.push(xhr);
        console.log("request sent to the server " + li.dataset.url);
    }
</script>
