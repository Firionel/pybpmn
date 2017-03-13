
from .base import BpmnDiagramModelObject


class BpmnLabel(BpmnDiagramModelObject):

    __tag_names = ('BPMNLabel', )
    __child_refs = {'bounds': 'Bounds'}


