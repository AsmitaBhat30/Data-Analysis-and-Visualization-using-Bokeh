from datetime import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource,DatetimeTickFormatter,NumeralTickFormatter

movieName = ['Forrest Gump','Saving Private Ryan','Pearl Harbor','Dunkirk','Gladiator','The Perfect Storm','Apollo 13','The Help','Straight Outta Compton','The Great Gatsby','The Truman Show','The Fault in our Stars','Inglourious Basterds','Seabiscuits','Lee Daniels The Butler','The Patriot','A Time to Kill','A League of Their Own','Phenomenon','Road to Perdition','Unforgiven','Contact','Public Enemies','Dead Poets Society','The Notebook','A.I. Artificial Intelligence']

y=[330252182,
212252181,
202512182,
190252182,
167025218,
150252182,
145252182,
138252182,
136252182,
129252182,
125092182,
123252182,
122652182,
121252182,
118252182,
116252182,
112252182,
111252182,
109252182,
107252182,
105252182,
104252182,
85252182,
87252182,
82252182,
75252182
]

x = [
datetime(1994,7,6),
datetime(1998,7,24),
datetime(2001,5,25),
datetime(2017,7,21),
datetime(2000,5,5),
datetime(2000,6,30),
datetime(1995,6,30),
datetime(2011,8,10),
datetime(2005,2,22),
datetime(1995,6,29),
datetime(1966,7,6),
datetime(2010,7,13),
datetime(2017,2,20),
datetime(1999,7,27),
datetime(1994,8,3),
datetime(1990,1,10),
datetime(2010,8,17),
datetime(2012,3,24),
datetime(1997,8,31),
datetime(2009,2,23),
datetime(1992,9,14),
datetime(2003,1,2),
datetime(1998,9,5),
datetime(1999,3,24),
datetime(2001,9,7),
datetime(1991,5,17),
]
output_file("moviegenre.html")
data_source = ColumnDataSource(data=dict(time=x,
                                    gross=y,
                                    names=movieName))
p = figure(title='Gross Earnings of top 26 Drama movies')

# scatter plot for the movies
p.scatter(x='time', y='gross', fill_color="red" ,size=8, source=data_source, name="points")

# labels for the axis
p.xaxis[0].axis_label = 'Year'
p.yaxis[0].axis_label = 'Gross Earning'

# formats for the axis
p.xaxis[0].formatter = DatetimeTickFormatter(years=["%Y"])
p.yaxis[0].formatter = NumeralTickFormatter(format="($ 0.00 a)")

# to show results
show(p)

