# DRAGONHACK 2020


### This repository consists of our code for the DragonHack 2020 entry. The project adresses the problems of oil spills and it hopefully spreads awareness. We combine multiple data sources to achive this goal. Our focus is heavily on the explotation of various statistics from this data sources.

### Contribution

- Marko Prelevikj, ++
- Gojko Hajduković, ++
- Boshko Koloski, ML/ ++
- Ferdi Jajai, UI

###

The backend code is developed with Python 3. To install the dependencies needed for reproduction of results run the following line.

`` pip3 install -r requirments.txt ``


## Initial data 

The data for the oil spils is obtained from the [Wikipedia](https://en.wikipedia.org/wiki/List_of_oil_spills) webpage. Since the table is incomplete and some key information were missing as exact coordinates. For such examples we fill the data manually as close as possible. Furthermoe we propose a way for this to be evaluated with an algorithmic apporoach for early detecion and awarness.


|Spill                                                        |Location                                                     |Dates                              |MinTonnes|MaxTonnes|Owner                                            |Coords                |
|-------------------------------------------------------------|-------------------------------------------------------------|-----------------------------------|---------|---------|-------------------------------------------------|----------------------|
|El Palito Refinery                                           |Venezuela, Golfo Triste                                      |8 August 2020                      |2,700    |2,700    |PetrÃ³leos de Venezuela                          |10.694448;-68.201062  |
|2020 Pointe D'Esny  MV Wakashio oil spill                    |Mauritius, Ile Aux Aigrettes and Mahebourg                   |25 July 2020                       |1,300    |4,300    |Wakashio Suisan Company Limited, Kagoshima, Japan|-20.438119;57.744631  |
|Trans Mountain oil spill                                     |Canada, British Columbia, Abbotsford                         |14 June 2020                       |118.5    |184.87   |Trans Mountain                                   |49.064499; -122.159002|
|Norilsk diesel fuel spill                                    |Russia, Norilsk, Krasnoyarsk Krai                            |29 May 2020                        |17,500   |17,500   |Nornickel                                        |69.379444;87.744444   |
|Tanker truck pumping out sludge from a vessel                |New Zealand, Tauranga, Bay of Plenty                         |30 March 2020                      |1.7      |1.7      |                                                 |-37.660155;176.231307 |





## Observation Hack
We use SINERGIZE's satelite imagery for detection of the oil leaks and comparison of between time stamps. For a given event we scan the coordinates and obtain the imagery in the interval of [day-30,day+30] and obtain a collection of images for the given oil spill. For such sequence of days the minimum number of images we obtained was 12 and the maximal number of images was 20.


## Data Mining Hack
### Sentiment analysis 
Since we wanted to capture the notion of how such events affect society, we proceeded by exploring the social medias. Particularlly we focused on the Twitter data the society tweets about for a given oil spill event. /
### Approach description
We scraped this data manually but also we provided an approach for it to be scraped automatically (Since Twitter recently updated their policies we went for the manual approach). 


After obtaining the data we extracted the sentiment and analyzed it through Ekman's 5 basic  emotions. We executed this analyiss with the ``text2emotion`` library.

### Graph Information

Since we live in connected world, for one to analyse the interactions and one needs a good representation. Natural representaton of such interactions are graphs. From them we can analyse the flows of events and intereacitons of entities.   /
With this in mind we generated a network of persons interactions based on their apperance on articles and papers. 

### Approach description

We used the ``googlesearch engine`` to search for links of articles and webpages containing information of oil spill events. For each oil spill event we took 30 pages and summarized them to up to 5 most representative sentences, for this we used the text-rank based extractor from the ``sumy`` library. \
After obtaining between 100 and 150 sentences for each oil spill we used Named Entity Recognition (NER) tool from which we extracted entity information. 
We modeled the graph in with the following heuristic, two entities were connected if they appeared in a single sentence. 

One such example of obtained graph is the following about the Pointe D'Esny MV Wakashio oil spil:

![Graph](data/graph.svg)


### Metainformation

From the NER information we extracted Organizations, Persons and Money values connected to the task.

### Integrity

Since this information is of vital character we want all of this to be secured we provide it's integrity by the power of BitCoin.


### Greater good hack

We believe that such an application would provide crucial information for spreading of awarness of the consequences for the ecosystem of oil spill events. 
### Project organization

- [Backend and Machine Learning logic](./be)
- [Frontend Logic](./fe) <- Webpage design
- [Data](./data) <- Scraped and serialized data 

