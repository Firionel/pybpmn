
from .activity import BpmnActivity


class BpmnSubProcess(BpmnActivity):

    __tag_names = ('subProcess', )
    __bpmn_attributes = ('triggeredByEvent', 'artifacts')


class BpmnTransaction(BpmnSubProcess):

    __tag_names = ('transaction', )
    __bpmn_attributes = ('method', )


class BpmnAdHocSubProcess(BpmnSubProcess):

    __tag_names = ('adHocSubProcess', )
    __bpmn_attributes = ('completionCondition', 'ordering', 'cancelRemainingInstances')