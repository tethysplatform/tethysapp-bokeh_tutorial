from bokeh.embed import server_document
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature
from django.shortcuts import render
import panel as pn
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from .param_model import ShapeViewer


@login_required()
def home(request):
    script = server_document(request.build_absolute_uri())
    context = {'script': script}
    return render(request, 'bokeh_tutorial/home.html', context)


def home_handler(document):
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

@login_required()
def shapes_with_panel(request):
    script = server_document(request.build_absolute_uri())
    context = {'script': script}
    return render(request, "bokeh_tutorial/shapes.html", context)


def shapes_handler(document):
    viewer = ShapeViewer()
    panel = pn.Row(viewer.param, viewer.panel())
    panel.server_doc(document)
