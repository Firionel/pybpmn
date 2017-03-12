
from ..base import BpmnFlowNode


class BpmnEvent(BpmnFlowNode):
    pass


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