
from ..base import BpmnModelObject

class Waypoint(BpmnModelObject):

    __tag_names = ('waypoint', )
    __bpmn_attributes = ('type', 'x', 'y')