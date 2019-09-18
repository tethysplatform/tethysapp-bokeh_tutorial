from tethys_sdk.base import TethysAppBase, url_map_maker


class BokehTutorial(TethysAppBase):
    """
    Tethys app class for Bokeh Tutorial.
    """

    name = 'Bokeh Tutorial'
    index = 'bokeh_tutorial:home'
    icon = 'bokeh_tutorial/images/icon.gif'
    package = 'bokeh_tutorial'
    root_url = 'bokeh-tutorial'
    color = '#2980b9'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='bokeh-tutorial',
                controller='bokeh_tutorial.controllers.home',
                handler='bokeh_tutorial.controllers.home_handler',
                handler_type='bokeh'
            ),
            UrlMap(
                name='shapes',
                url='bokeh-tutorial/shapes',
                controller='bokeh_tutorial.controllers.shapes_with_panel',
                handler='bokeh_tutorial.controllers.shapes_handler',
                handler_type='bokeh'
            ),
        )

        return url_maps