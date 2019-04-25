from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource,CategoricalColorMapper

house = ['Warner Bros.', 'Universal', 'Paramount', 'Buena Vista', '20th Century Fox', 'Sony / Columbia', 'Miramax', 'New Line', 'MGM/UA',
     'DreamWorks SKG', 'USA Films', 'Sony Classics', 'Lionsgate', 'Fox Searchlight', 'Newmarket', 'Paramount Classics', 'IMAX',
     'Fine Line', 'Artisan', '8X Entertainment', 'Focus Features', 'WGB.', 'First Look', 'N Wave', 'Samuel Goldwyn', 'IDP']

y = [15.1, 11.7, 11.0, 10.9, 10.6, 9.0,7.5,6.7,5.5,4.9,1.7,1.7,0.7,0.6,0.3,0.3,0.3,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
x=[27,13,14,14,16,25,25,9,11,5,11,11,17,4,2,7,3,3,5,2,5,1,4,1,1,5]
colors=['gold','silver','grey','black','navy','blue','purple','violet','turquoise','magenta','azure','teal','cyan','green','lime','chartreuse','olive','yellow','gold','plum','orange','brown','red','maroon','pink','tan']
source = ColumnDataSource(data=dict(x=x,y=y,house=house))
# output to static HTML file
output_file("filmhouse.html")
TOOLTIPS = [
    ("House", "@house"),
]
p = figure( title="Movie House Market Share", plot_width=1500, x_axis_label='Number of Movies', y_axis_label='Market Share in %',x_range=(0,35),tooltips=TOOLTIPS)
color_mapper = CategoricalColorMapper(factors=house, palette=colors)
p.circle(
    x='x', y='y',source=source,
    color={'field': 'house', 'transform': color_mapper},
    legend='house',size='x'
)
show(p)


