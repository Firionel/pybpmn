
from ..base import BpmnBaseObject


class BpmnMessageFlow(BpmnBaseObject):

    __tag_names = ('messageFlow', )
    __bpmn_attributes = ('name', 'sourceRef', 'targetRef', 'messageRef')