
from ..base import BpmnFlowNode


class BpmnActivity(BpmnFlowNode):

    __bpmn_attributes = ('isForCompensation', 'loopCharacteristics', 'resources', 'default', 'ioSpecification'
                         , 'properties', 'boundaryEventRefs', 'dataInputAssociations', 'dataOutputAssociations'
                         , 'startQuantity', 'completionQunatity')

    def _create_dom_outline(self, document):
        outline_element = document.createElement("rect")
        outline_element.setAttribute("x", "0")
        outline_element.setAttribute("y", "0")
        outline_element.setAttribute("width", "100")
        outline_element.setAttribute("height", "75")
        return outline_element
