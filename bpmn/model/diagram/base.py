
from ..base import BpmnBaseObject


class BpmnDiagramBaseObject(BpmnBaseObject):

    __bpmn_attributes = ('bpmnElement', )
    __child_refs = {'bounds': 'Bounds'}


class BpmnLabelledDiagramBaseObject(BpmnDiagramBaseObject):

    _child_refs = {'labels': 'BPMNLabel'}