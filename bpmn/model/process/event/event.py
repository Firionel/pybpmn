
from ..base import BpmnFlowNode


class BpmnEvent(BpmnFlowNode):

    def create_dom_shape(self, document):
        shape_element = document.createElement("circle")
        shape_element.setAttribute("cx", "18")
        shape_element.setAttribute("cy", "18")
        shape_element.setAttribute("r", "18")
        return shape_element


class BpmnThrowEvent(BpmnEvent):

    __bpmn_attributes = ('inputSet', )


class BpmnIntermediateThrowEvent(BpmnThrowEvent):

    __tag_names = ('intermediateThrowEvent', )


class BpmnEndEvent(BpmnThrowEvent):

    __tag_names = ('endEvent', )


class BpmnCatchEvent(BpmnEvent):

    __bpmn_attributes = ('parallelMultiple', 'outputSet')


class BpmnStartEvent(BpmnCatchEvent):

    __tag_names = ('startEvent', )


class BpmnIntermediateCatchEvent(BpmnCatchEvent):

    __tag_names = ('intermediateCatchEvent', )


class BpmnBoundaryEvent(BpmnCatchEvent):

    __tag_names = ('boundaryEvent', )
    __bpmn_attributes = ('cancelActivity', 'attachedToRef')