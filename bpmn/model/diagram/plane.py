
from .base import BpmnDiagramBaseObject


class BpmnPlane(BpmnDiagramBaseObject):

    __tag_names = ('BPMNPlane', )
    __child_refs = {'shapes': 'BPMNShape', 'edges': 'BPMNEdge'}
