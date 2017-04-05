
from ..base import BpmnBaseObject


class BpmnEventDefinition(BpmnBaseObject):
    pass


class BpmnMessageEventDefinition(BpmnEventDefinition):
    pass


class BpmnEscalationEventDefinition(BpmnEventDefinition):
    pass


class BpmnErrorEventDefinition(BpmnEventDefinition):
    pass


class BpmnCompensationEventDefinition(BpmnEventDefinition):
    pass


class BpmnSignalEventDefinition(BpmnEventDefinition):
    pass


class BpmnTerminateEventDefinition(BpmnEventDefinition):
    pass


class BpmnTimerEventDefinition(BpmnEventDefinition):
    pass


class BpmnConditionalEventDefinition(BpmnEventDefinition):
    pass


class BpmnLinkEventDefinition(BpmnEventDefinition):
    pass
