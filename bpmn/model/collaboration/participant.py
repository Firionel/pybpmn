
from ..base import BpmnBaseObject


class BpmnParticipant(BpmnBaseObject):

    __tag_names = ('participant', )
    __bpmn_attributes = ('name', 'processRef', 'partnerRoleRef', 'partnerRoleRef', 'partnerEntityRef'
                         , 'interfaceRef', 'participantMultiplicity', 'endPointRefs')
