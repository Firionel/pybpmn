
from ..base import BpmnBaseObject


class BpmnDiagram(BpmnBaseObject):

    __tag_names = ('BPMNDiagram', )
    __child_refs = {'planes': 'BPMNPlane'}

