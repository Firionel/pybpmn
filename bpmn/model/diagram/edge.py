
from .base import BpmnLabelledDiagramBaseObject


class BpmnEdge(BpmnLabelledDiagramBaseObject):

    __tag_names = ('BPMNEdge', )
    __bpmn_attributes = ('messageVisibleKind', )
    __child_refs = {'waypopints': 'waypoint'}
