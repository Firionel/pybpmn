
from .base import BpmnLabelledDiagramBaseObject, BoundedDiagramMixin


class BpmnShape(BoundedDiagramMixin, BpmnLabelledDiagramBaseObject):

    __tag_names = ('BPMNShape', )
    __bpmn_attributes = ('isHorizontal', 'isExpanded', 'isMarkerVisible', 'isMessageVisible', 'participantBandKind')
    __style = {"fill": "white"}

    def _create_dom_element(self, document):
        shape_element = self.referenced_bpmn_element.create_dom_shape(document)
        return shape_element


