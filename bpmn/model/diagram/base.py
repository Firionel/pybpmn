
from ..base import BpmnModelObject, BpmnBaseObject


class BpmnDiagramModelObject(BpmnModelObject):

    __child_refs = {'bounds': 'Bounds'}


class BpmnDiagramBaseObject(BpmnDiagramModelObject, BpmnBaseObject):

    __bpmn_attributes = ('bpmnElement', )

    @property
    def referenced_bpmn_element(self):
        return self.definitions.get_item_by_id(self.bpmnElement)

    def svg_string(self):
        return ''


class BpmnLabelledDiagramBaseObject(BpmnDiagramBaseObject):

    _child_refs = {'labels': 'BPMNLabel'}

    def _svg_envelope(self):
        return '<g data-element-id="%s" transform="translate(%d, %d)">' % (self.referenced_bpmn_element.id
                                                                           , self.x, self.y)
    def _label_svg(self, label):
        return '<text><tspan '