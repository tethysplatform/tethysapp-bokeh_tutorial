from tethys_sdk.base import TethysAppBase


class App(TethysAppBase):
    """
    Tethys app class for Bokeh Tutorial.
    """
    name = 'Bokeh Tutorial'
    description = ''
    package = 'bokeh_tutorial'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'bokeh-tutorial'
    color = '#27ae60'
    tags = ''
    enable_feedback = False
    feedback_emails = []
