from manimlib import *

class Pyramid(VGroup):
    CONFIG = {
        "height": 2,
        "width": 2,
        "fill_color": BLUE,
        "fill_opacity": 0.5,}
    def __init__(self,side, **kwargs):
        self.side = side 
        s= self.side 
        super().__init__(**kwargs)
        top = PyramidTop(s)
        self.add(
            top,
            *[  Polygon(
                    *top.vertices[0:2],
                    [0,0,self.height],**kwargs),
                Polygon(
                    *top.vertices[1:3],
                    [0,0,self.height],**kwargs),
                Polygon(
                    *top.vertices[2:4],
                    [0,0,self.height],**kwargs),
                Polygon(
                   top.vertices[-1],
                   top.vertices[0],
                   [0,0,self.height],**kwargs),])

class PyramidTop(Polygon):
    CONFIG = {}
    def __init__(self,side= 3, **kwargs):
        self.side = side
        s = self.side 
        digest_config(self,self.CONFIG)
        
        vertices = [
          [-s/2, -s/2, 0],
          [ s/2, -s/2, 0],
          [ s/2, s/2,  0],
          [-s/2, s/2,  0]]
      
        super().__init__(*vertices,**kwargs)
        

