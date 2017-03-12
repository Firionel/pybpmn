
from ..base import BpmnModelObject


class Bounds(BpmnModelObject):

    __tag_names = ('Bounds', )
    __bpmn_attributes = ('x', 'y', 'width', 'height')
