
from ..base import BpmnFlowNode


class BpmnGateway(BpmnFlowNode):

    __tag_names = ('gatewayDirection', )


class BpmnExclusiveGateway(BpmnGateway):

    __tag_names = ('exclusiveGateway', )


class BpmnInclusiveGateway(BpmnGateway):

    __tag_names = ('inclusiveGateway',)


class BpmnParallelGateway(BpmnGateway):

    __tag_names = ('parallelGateway',)


class BpmnComplexGateway(BpmnGateway):

    __tag_names = ('complexGateway', )


class BpmnEventBasedGateway(BpmnGateway):

    __tag_names = ('eventBasedGateway', )
    __bpmn_attributes = ('instantiate', 'eventGatewayType')
