# flask-death-demo
A demo of a flask app to show "leading causes of death in US".  Fun times.

Data is from here: <https://catalog.data.gov/dataset/age-adjusted-death-rates-for-the-top-10-leading-causes-of-death-united-states-2013>

The JSON file from that site was retrieved on November 21, 2018, and is in the top level directory under data as death.json

The directory `explore/` has some Python code for exploring the data to better understand the structure of the file.

If you cd into `explore` you can then run either `python -i explore_death.py` or `python3 -i explore_death.py` and
you'll get a Python prompt where the variable `d` contains the entire contents of `death.json` as a Python dictionary.

The file [explore.md](explore.md) contains a sample session 

