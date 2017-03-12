
from ..base import BpmnBaseObject, BpmnModelObject


class BpmnFlowElement(BpmnBaseObject):
    __bpmn_attributes = ('name', )


class BpmnFlowNode(BpmnFlowElement):

    @property
    def successors(self):
        outbound_flows = [flow for flow in self.definitions.get_items_by_tag_name('sequenceFlow') if
                          flow.sourceRef == self.id]
        return [self.definitions.get_item_by_id(flow.targetRef) for flow in outbound_flows if flow.targetRef]

    @property
    def precursors(self):
        inbound_flows = [flow for flow in self.definitions.get_items_by_tag_name('sequenceFlow') if
                         flow.targetRef == self.id]
        return [self.definitions.get_item_by_id(flow.sourceRef) for flow in inbound_flows if flow.sourceRef]


class BpmnReference(BpmnModelObject):

    def __init__(self, *args, **kwargs):
        self.reference_id = None
        super(BpmnReference, self).__init__(*args, **kwargs)

    @classmethod
    def _set_attributes_from_node(cls, node, instance):
        data_children = [child for child in node.childNodes if child.nodeType == node.TEXT_NODE]
        if data_children:
            instance.reference_id = data_children[0].data
