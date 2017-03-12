
from ..base import BpmnFlowNode


class BpmnActivity(BpmnFlowNode):

    __bpmn_attributes = ('isForCompensation', 'loopCharacteristics', 'resources', 'default', 'ioSpecification'
                         , 'properties', 'boundaryEventRefs', 'dataInputAssociations', 'dataOutputAssociations'
                         , 'startQuantity', 'completionQunatity')

