
from ..base import BpmnBaseObject


class BpmnCollaboration(BpmnBaseObject):

    __tag_names = ('collaboration',)
    __bpmn_attributes = ('name', 'isClosed')
