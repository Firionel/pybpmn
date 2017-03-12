
from .base import BpmnLabelledDiagramBaseObject


class BpmnShape(BpmnLabelledDiagramBaseObject):

    __tag_names = ('BPMNShape', )
    __bpmn_attributes = ('isHorizontal', 'isExpanded', 'isMarkerVisible', 'isMessageVisible', 'participantBandKind')
