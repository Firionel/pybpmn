
from ..base import BpmnDiagramModelObject


class Waypoint(BpmnDiagramModelObject):

    __tag_names = ('waypoint', )
    __bpmn_attributes = ('type', 'x', 'y')