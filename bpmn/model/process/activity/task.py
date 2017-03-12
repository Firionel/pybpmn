
from .activity import BpmnActivity


class BpmnTask(BpmnActivity):

    __tag_names = ('task', )


class BpmnServiceTask(BpmnTask):

    __tag_names = ('serviceTask', )
    __bpmn_attributes = ('implementation', 'operationRef')


class BpmnSendTask(BpmnTask):

    __tag_names = ('sendTask', )
    __bpmn_attributes = ('messageRef', 'operationRef', 'implementation')


class BpmnReceiveTask(BpmnTask):

    __tag_names = ('receiveTask', )
    __bpmn_attributes = ('messageRef', 'instantiate', 'operationRef', 'implementation')


class BpmnUserTask(BpmnTask):

    __tag_names = ('userTask', )
    __bpmn_attributes = ('implementation', 'renderings')


class BpmnManualTask(BpmnTask):

    __tag_names = ('manualTask', )


class BpmnBusinessRuleTask(BpmnTask):

    __tag_names = ('businessRuleTask', )
    __bpmn_attributes = ('implementation', )


class BpmnScriptTask(BpmnTask):

    __tag_names = ('scriptTask', )
    __bpmn_attributes = ('scriptFormat', 'script')

