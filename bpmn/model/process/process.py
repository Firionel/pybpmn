from ..base import BpmnBaseObject


class BpmnProcess(BpmnBaseObject):

    __tag_names = ('process', )
    __bpmn_attributes = ('processType', 'isExecutable', 'auditing', 'monitoring', 'artifacts', 'isClosed', 'supports'
                         , 'properties', 'resources', 'correlationSubscriptions', 'definitionalCollaborationRef')
