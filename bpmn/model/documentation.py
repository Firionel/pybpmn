
from .base import BpmnModelObject


class BpmnDocumentation(BpmnModelObject):

    __tag_names = ('documentation', )
    __bpmn_attributes = ('text', 'textFormat')
