
from .base import BpmnLabelledDiagramBaseObject


class BpmnEdge(BpmnLabelledDiagramBaseObject):

    __tag_names = ('BPMNEdge', )
    __bpmn_attributes = ('messageVisibleKind', )
    __child_refs = {'waypoints': 'waypoint'}

    @property
    def x(self):
        return min([int(waypoint.x) for waypoint in self.waypoints])

    @property
    def y(self):
        return min([int(waypoint.y) for waypoint in self.waypoints])

    @property
    def width(self):
        return max([int(waypoint.x) for waypoint in self.waypoints]) - self.x

    @property
    def height(self):
        return max([int(waypoint.y) for waypoint in self.waypoints]) - self.y

    def _create_dom_element(self, document):
        path_element = document.createElement("path")
        path_element.setAttribute("d", self._get_path_string())
        path_element.setAttribute("marker-end", "url(#edge-end-cap)")
        return path_element

    def _get_path_string(self):
        points = ["%s %s" % (waypoint.x, waypoint.y) for waypoint in self.waypoints]
        return 'M ' + points[0] + ''.join(' L' + point for point in points[1:])
