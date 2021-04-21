# 🌏🌍🌎    GEOSPATIAL DATA PROJECT    🌏🌍🌎

<img width=500 src=https://media.giphy.com/media/l378asbpIR5DTsdqg/giphy.gif>

## Goal 🏁
This is a python project that was sent to us at the Ironhack data analytics bootcamp. 

The objective of the project is to select the location of a `gaming company` offices with the following structure:
* 20 Designers
* 5 UI/UX Engineers
* 10 Frontend Developers
* 15 Data Engineers
* 5 Backend Developers
* 20 Account Managers
* 1 Maintenance guy that loves basketball
* 10 Executives
* 1 CEO/President

The location has to cover more or less this requirements:

* Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
* 30% of the company staff have at least 1 child.
* Developers like to be near successful tech startups that have raised at least 1 Million dollars.
* Executives like Starbucks A LOT. Ensure there's a starbucks not too far.
* Account managers need to travel a lot.
* Everyone in the company is between 25 and 40, give them some place to go party.
* The CEO is vegan.
* If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
* The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.

## Tools ⚙️
The tools to be used are functions, string operations, pandas, mongo queries and geoqueries, requests from APIs, plotting maps, error handling etc. 

## Libraries 👩🏼‍🏫
- [Pandas](https://pandas.pydata.org/docs/)
- [Requests](https://docs.python-requests.org/en/master/)
- [Os](https://docs.python.org/3/library/os.html)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Re](https://docs.python.org/3/library/re.html)
- [Numpy](https://numpy.org/doc/)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [Folium](https://python-visualization.github.io/folium/)
- [Geopandas](https://geopandas.org/)
- [Json](https://docs.python.org/3/library/json.html)
- [KeplerGl](https://kepler.gl/)

## My project 👩🏼‍💻
The final location will be the location of an existing company. 

To find the ideal location, the first decision to make is in which city it will be situated. 🏙

From a list of 18.8K companies, design and tech startups with a high net worth are selected. 

Once this pre-selection is done, the cities chosen will be the top 3 cities with the highest number of companies. 

Then, (thanks to the foursquare API) some establishments that meet employee preferences in the 3 cities are located. 

Once all these sites located, for each selected company in the 3 cities, it is looked at how many of these sites there are nearby. 

To choose the final location, a weighted score is given based on how many sites are close by and the importance of having these sites close by. The one with the best score is selected. 

## Content of the repository 👀

- Src folder with the functions defined and documented
- Jupyter Notebooks with the main programs
- Environment.yml and requirements.txt
- Data folder with the dataframes created
- Json folder with the jsons created (and imported to MongoDB)
- Maps folder with the maps created 

## Further lines
- Try folium.features.CustomIcon("....png")
- More sophisticated selection of locations (give value according to proximity)

