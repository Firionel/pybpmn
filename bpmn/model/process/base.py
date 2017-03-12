
from ..base import BpmnBaseObject


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
