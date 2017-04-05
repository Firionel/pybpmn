
from .base import BpmnDiagramBaseObject, BoundedDiagramMixin


class BpmnPlane(BpmnDiagramBaseObject):

    __tag_names = ('BPMNPlane', )
    __child_refs = {'shapes': 'BPMNShape', 'edges': 'BPMNEdge'}

    @property
    def diagram_elements(self):
        return self.shapes + self.edges

    @property
    def width(self):
        return max([el.x + el.width for el in self.diagram_elements] + [0]) \
               - min([el.x for el in self.diagram_elements] + [0])

    @property
    def height(self):
        return max([el.y + el.height for el in self.diagram_elements] + [0]) \
               - min([el.y for el in self.diagram_elements] + [0])

