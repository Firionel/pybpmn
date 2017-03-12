
from .base import BpmnFlowElement


class BpmnSequenceFlow(BpmnFlowElement):

    __tag_names = ('sequenceFlow', )
    __bpmn_attributes = ('isImmediate', 'sourceRef', 'targetRef', 'conditionExpression')
