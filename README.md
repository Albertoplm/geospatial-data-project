# geospatial-data-project

![futuristic-map](https://github.com/Albertoplm/geospatial-data-project/blob/main/images/futuristic-map.jpg)


### Office requirements

- **Nearby companies that also do design.**
- **30% of the company staff have at least 1 child**
- **Developers like to be near successful tech startups that have raised at least 1 Million dollars.**
- **Executives like Starbucks A LOT.**
- **Account managers need to travel a lot.**
- **Give them some place to go party.**
- **The CEO is vegan.**
- **Maintenance guy, a basketball stadium must be around 10 Km.**
- **The office dog—"Dobby" needs a hairdresser every month**

### Let´s do it

First of all I check the companies database in order to find offices in Madrid, so I ask to the database for Web companies offices, because I trully believe that they are the coolest. And we are going to steal one from them!

The next step is to search for companies of the tech industry in Madrid in order to check if they are near to the possible office or not.

Once I have this, I start with the geoqueries, for this I used Foursquare API.

Then I check what is the best office, what office fulfill the requierements.

Finally I used folium to create a beatifull map. 

### Structure of the repo

In this repo you may find:

    - Data: A folder with the .json of the geoqueries and the .csv of the dataframes
    - Images: All the Icons of the fantastic map!
    - Src: The functions that I have used.
    - Database.ipynb: List of possible offices in Madrid
    - Competency.ipynb: List of tech companies offices in Madrid
    - Queries.ipynb: All the Foursquare queries and all the checking in order to choose the best option
    - Maps.ipynb: The Madrid map with all the venues and offices
    
### Libraries used to carry out the project

- [Pymongo Geosphere](https://pymongo.readthedocs.io/en/stable/examples/geo.html)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/es/latest/)
- [Json](https://www.w3schools.com/python/python_json.asp)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Os](https://docs.python.org/3/library/os.html)
- [Folium](https://python-visualization.github.io/folium/)