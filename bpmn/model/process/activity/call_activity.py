
from .activity import BpmnActivity


class BpmnCallActivity(BpmnActivity):

    __tag_names = ('callActivity', )
    __bpmn_attributes = ('calledElement', )