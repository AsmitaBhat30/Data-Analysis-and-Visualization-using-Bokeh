from datetime import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter
from bokeh.transform import dodge
from bokeh.core.properties import value
from bokeh.io import output_notebook

output_notebook()

# create output filea
output_file("genrecountries.html")

# countries for foreign market
countries=["Argentina",
"Australia",
"Belgium",
"Brazil",
"China",
"Colombia"
]

# top 5 movies for the genre
top_movies=[
"Forrest Gump",
"Saving Private Ryan",
"Pearl Harbor",
"Dunkirk",
"Gladiator"
]

# gross earnings of the top 5 movies in the foreign market
fGump=[4999308,
22839211,
5562917,
5381320,
5062459,
6865078]

pvtRyan=[4376869,
46822002,
5654123,
6681146,
9543153,
3268925]

pHrbr=[3331732,
54385465,
4061231,
6904807,
6300000,
7140604]

Dnkrk=[2310437,
33829034,
5003952,
7569037,
1473064,
1507057]

Gldtr=[1480477,
39880001,
4435611,
20156555,
0,
3651300]


data = {"countries" : countries,
        top_movies[0]   : fGump,
        top_movies[1]   : pvtRyan,
        top_movies[2]   : pHrbr,
        top_movies[3]   : Dnkrk,
        top_movies[4]   : Gldtr}

source = ColumnDataSource(data=data)

# create a new plot with a title y_axis range and plot height
p = figure(x_range=countries, y_range=(0,400000000),plot_height=450,title="")

# creating bar charts for the top 5 movies with color codes
p.vbar(x=dodge('countries', -0.34, range=p.x_range), top=top_movies[0], width=0.15,
       source=source,color="#c9d9d3", legend=value(top_movies[0]))

p.vbar(x=dodge('countries', -0.17, range=p.x_range), top=top_movies[1], width=0.15,
       source=source,color="#718dbf", legend=value(top_movies[1]))

p.vbar(x=dodge('countries',  0.0,  range=p.x_range), top=top_movies[2], width=0.15,
       source=source,color="#e84d60", legend=value(top_movies[2]))

p.vbar(x=dodge('countries',  0.17, range=p.x_range), top=top_movies[3], width=0.15,
       source=source,color="#008000", legend=value(top_movies[3]))

p.vbar(x=dodge('countries',  0.34, range=p.x_range), top=top_movies[4], width=0.15,
       source=source,color="#cd853f", legend=value(top_movies[4]))

# creating format for the y axis lables
p.yaxis[0].formatter = NumeralTickFormatter(format="($ 0.00 a)")

# removing the x axis grid
p.xgrid.grid_line_color = None

# positioning the legend
p.legend.location = "top_left"
p.legend.orientation = "vertical"

# to show the result
show(p)