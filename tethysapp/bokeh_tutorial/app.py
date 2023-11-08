from tethys_sdk.base import TethysAppBase


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
