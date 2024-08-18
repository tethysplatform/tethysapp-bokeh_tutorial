from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import column
from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature

from tethys_sdk.routing import handler

from .param_model import ShapeViewer

@handler(
    template="bokeh_tutorial/home.html",
)
def home(document):
    df = sea_surface_temperature.copy()
    source = ColumnDataSource(data=df)

    plot = figure(x_axis_type="datetime", y_range=(0, 25), y_axis_label="Temperature (Celsius)",
                  height=500, width=800, title="Sea Surface Temperature at 43.18, -70.43")
    plot.line("time", "temperature", source=source)

    slider = Slider(start=0, end=30, value=0, step=1, title="Smoothing by N Days")

    def callback(attr, old, new):
        if new == 0:
            data = df
        else:
            data = df.rolling(f'{new}D').mean()
        source.data = dict(ColumnDataSource(data=data).data)

    slider.on_change("value", callback)

    document.add_root(column(slider, plot))

@handler(
    app_package='bokeh_tutorial',
)
def shapes(document):
    breakpoint()
    
    request = document.session_context.request

    viewer = ShapeViewer().panel()
    viewer.server_doc(document)

    