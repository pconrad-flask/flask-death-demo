# flask-death-demo
A demo of a flask app to show "leading causes of death in US".  Fun times.

Data is from here: <https://catalog.data.gov/dataset/age-adjusted-death-rates-for-the-top-10-leading-causes-of-death-united-states-2013>

The JSON file from that site was retrieved on November 21, 2018, and is in the top level directory under data as death.json

The directory `explore/` has some Python code for exploring the data to better understand the structure of the file.

If you cd into `explore` you can then run either `python -i explore_death.py` or `python3 -i explore_death.py` and
you'll get a Python prompt where the variable `d` contains the entire contents of `death.json` as a Python dictionary.

The file [explore.md](explore.md) contains a sample session 

After exploring the data, we learned that:
* There are 10296 rows of data

   ```
   >>> len(d['data'])
   10296
   >>> 
   ```   
* The five most interesting fields in the data are: 8,10,11,12,13 (inclusive:
   * Year (int, 4 digits)
   * Cause Name (string)
   * State (string, full state name)
   * Deaths (int)
   * Age-Adjusted Death Rate (float)
   
So, the next step might be to write a short program that converts the raw deaths.json file into a compact_deaths.json
that has only the data that we think will be useful in the webapp.

That file might have the form of of a simple list of dictionaries.  Where `d['data'][0]` looked like this:

```
>>> d['data'][0]
[15029, '0E3080FB-5EF8-4BEF-834E-54B52DB8DFF3', 15029, 1534786069, '1099577', 1534786069, '1099577', None, '2016', 'Accidents (unintentional injuries) (V01-X59,Y85-Y86)', 'Unintentional injuries', 'Alabama', '2755', '55.5']
>>> 
```

In our new `deaths_compact.json` that row would simply be:

```
>>> cd[0]
{'year':'2016', 'cause':'Unintentional injuries', 'state':'Alabama', 'deaths':'2755', 'rate':'55.5'}
>>> 
```

So, we'd have a much easier data structure to work with.

That code is in the directory `simplify`
