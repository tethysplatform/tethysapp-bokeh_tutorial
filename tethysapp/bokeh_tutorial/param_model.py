import param
import panel as pn
import numpy as np
from bokeh.plotting import figure


class Shape(param.Parameterized):
    radius = param.Number(default=1, bounds=(0, 1))

    def __init__(self, **params):
        super(Shape, self).__init__(**params)
        self.figure = figure(x_range=(-1, 1), y_range=(-1, 1), width=500, height=500)
        self.renderer = self.figure.line(*self._get_coords())

    def _get_coords(self):
        return [], []

    def view(self):
        if not self.figure.renderers:
            self.__init__(name=self.name)
        return self.figure


class Circle(Shape):
    n = param.Integer(default=100, precedence=-1)

    def __init__(self, **params):
        super(Circle, self).__init__(**params)

    def _get_coords(self):
        angles = np.linspace(0, 2 * np.pi, self.n + 1)
        return (self.radius * np.sin(angles),
                self.radius * np.cos(angles))

    @param.depends('radius', watch=True)
    def update(self):
        xs, ys = self._get_coords()
        self.renderer.data_source.data.update({'x': xs, 'y': ys})


class NGon(Circle):
    n = param.Integer(default=3, bounds=(3, 10), precedence=1)

    @param.depends('radius', 'n', watch=True)
    def update(self):
        xs, ys = self._get_coords()
        self.renderer.data_source.data.update({'x': xs, 'y': ys})


shapes = [NGon(name='NGon'), Circle(name='Circle')]


class ShapeViewer(param.Parameterized):
    shape = param.ObjectSelector(default=shapes[0], objects=shapes)

    @param.depends('shape')
    def view(self):
        return self.shape.view()

    @param.depends('shape', 'shape.radius')
    def title(self):
        return '## %s (radius=%.1f)' % (type(self.shape).__name__, self.shape.radius)

    @param.depends('shape')
    def controls(self):
        return pn.Param(self.shape)

    def panel(self):
        expand_layout = pn.Column()

        return pn.Column(
            pn.pane.HTML('<h1>Bokeh Integration Example using Param and Panel</h1>'),
            pn.Row(
                pn.Column(
                    pn.panel(self.param, expand_button=False, expand=True, expand_layout=expand_layout),
                    "#### Subobject parameters:",
                    expand_layout),
                pn.Column(self.title, self.view)
            ),
            sizing_mode='stretch_width',
        )