import sys 
sys.path.append(".")

from manimlib import *
from pyramid import Pyramid


class TestPyramid(Scene):

    def construct(self):

        p = Pyramid(3)

        self.play(Write(p), run_time = 2.5)

        self.wait(3)

        self.camera.frame.add_updater(
            lambda m,dt: m.rotate(angle = dt, axis = [1,1,0]))

        self.wait(5)

class PyramidsScene(Scene):
    def construct(self):
        pyramids = VGroup()
        for i in range(100):
            pyramid = Pyramid(3)
            pyramid.shift(2 * RIGHT * i)
            pyramid.rotate(i, UP)
            pyramids.add(pyramid)

        pyramids.arrange_in_grid(10,10)
        pyramids.set_height(7)

        self.play(
            LaggedStart(*[
                Rotate(pyramid, radians=TAU/16, axis=UP)
                for pyramid in pyramids
            ])
        )
        self.wait()
