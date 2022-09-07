from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.routing import register_controllers


class BokehTutorial(TethysAppBase):
    """
    Tethys app class for Bokeh Tutorial.
    """

    name = 'Bokeh Tutorial'
    index = 'home'
    package = 'bokeh_tutorial'  # WARNING: Do not change this value
    icon = f'{package}/images/icon.gif'
    root_url = 'bokeh-tutorial'
    color = '#2980b9'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []
