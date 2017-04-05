
from cStringIO import StringIO

from ..base import BpmnBaseObject


class BpmnDiagram(BpmnBaseObject):

    __tag_names = ('BPMNDiagram', )
    __child_refs = {'planes': 'BPMNPlane'}

    @property
    def width(self):
        return max([pl.width for pl in self.planes])

    @property
    def height(self):
        return max([pl.height for pl in self.planes])

    def write_to_document(self, document):
        diagram_element = document.documentElement
        diagram_element.setAttribute("height", '%d' % self.height)
        diagram_element.setAttribute("width", '%d' % self.width)
        diagram_element.setAttribute("viewBox", "%d %d %d %d" % (0, 0, self.width, self.height))

        self._add_markers_to_document(document)
        for child in self.children():
            child.add_to_dom_element(diagram_element, document)

    def _add_markers_to_document(self, document):
        marker_element = document.createElement("marker")
        marker_element.setAttribute("id", "edge-end-cap")
        marker_element.setAttribute("viewBox", "0 0 20 20")
        marker_element.setAttribute("orient", "auto")
        marker_element.setAttribute("markerUnits", "strokeWidth")
        marker_element.setAttribute("markerWidth", "10")
        marker_element.setAttribute("markerHeight", "7")
        marker_element.setAttribute("refX", "20")
        marker_element.setAttribute("refY", "10")
        path_element = document.createElement("path")
        path_element.setAttribute("d", "M 0 0 L 20 10 L 0 20 z")
        marker_element.appendChild(path_element)
        document.documentElement.appendChild(marker_element)