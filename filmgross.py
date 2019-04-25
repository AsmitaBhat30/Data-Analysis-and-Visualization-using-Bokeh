from datetime import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.models import NumeralTickFormatter,ColumnDataSource,LabelSet

#Movie Avengers

# prepare some data
x = [
datetime(18,4,27),
datetime(18,5,4),
datetime(18,5,11),
datetime(18,5,18),
datetime(18,5,25),
datetime(18,6,1),
datetime(18,6,8),
datetime(18,6,15),
datetime(18,6,22),
datetime(18,6,29),
datetime(18,7,6),
datetime(18,7,13),
datetime(18,7,20),
datetime(18,7,27),
datetime(18,8,3),
datetime(18,8,10),
datetime(18,8,17),
datetime(18,8,24),
datetime(18,8,31),
datetime(18,9,7)
]

y = [338332540, 147679563, 80348856, 38833679, 27304294, 15398767, 11006251, 8080499, 4098263,
     2846762,1473963,1030085,722556,660755,399274,274762,139811,76484,81539,26779
]
rank=['1','1','1','2','3','4','5','8','9','13','15','16','21','22','26','29','41','48','48','57']

source = ColumnDataSource(data=dict(x=x,
                                    y=y,
                                    rank=rank))
output_file("filmgross.html")

p = figure( title="Avengers - Infinity War Gross to date", plot_width=1200, x_axis_label='Date', y_axis_label='Weekly Gross',
            x_axis_type="datetime")

p.line( x, y, legend="Weekly Gross", line_width=2 )
p.scatter(x='x', y='y',color='red',size=8, source=source, legend="Rank of the movie")
labels = LabelSet(x='x', y='y', text='rank', level='glyph',x_offset=5, y_offset=5, source=source, render_mode='canvas')
p.yaxis[0].formatter = NumeralTickFormatter(format="($ 0.00 a)")
p.add_layout(labels)
show(p)


