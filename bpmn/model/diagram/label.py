
from .base import BpmnDiagramModelObject, BoundedDiagramMixin


class BpmnLabel(BpmnDiagramModelObject, BoundedDiagramMixin):

    __tag_names = ('BPMNLabel', )
    __child_refs = {'bounds': 'Bounds'}

    def add_to_dom_element(self, element, document):
        #labels are added by their parents directly
        pass