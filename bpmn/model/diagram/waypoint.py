
from .base import BpmnDiagramModelObject


class Waypoint(BpmnDiagramModelObject):

    __tag_names = ('waypoint', )
    __bpmn_attributes = ('type', 'x', 'y')

    def add_to_dom_element(self, element, document):
        pass
