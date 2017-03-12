
from xml.dom.minidom import Node

from base import BpmnBaseObject, BpmnModelObject
from exceptions import NoResponsibleClass, ResponsibleClassAmbiguous


class BpmnDefinitions(BpmnBaseObject):

    __tag_names = ('definitions', )
    __bpmn_attributes = ('name', 'targetNamespace', 'expressionLanguage', 'typeLanguage', 'exporter', 'exporterVersion')

    def __init__(self, element_id):
        super(BpmnDefinitions, self).__init__(element_id, self)
        self._object_register = {}

    def register(self, bpmn_object):
        # do not register self during constructor of base objecct
        if bpmn_object is self:
            return

        self._object_register[bpmn_object.access_id] = bpmn_object

    @classmethod
    def from_dom_node(cls, parent_definitions, node):
        element_id = cls._element_id_from_node(node)
        instance = cls(element_id)
        cls._set_attributes_from_node(node, instance)

        for child_node in node.childNodes:
            if child_node.nodeType != Node.ELEMENT_NODE:
                continue
            try:
                BpmnModelObject.from_dom_node(instance, child_node)
            except NoResponsibleClass:
                pass
            except ResponsibleClassAmbiguous:
                pass

        return instance

    def get_item_by_id(self, element_id):
        return self._object_register[element_id]

    def get_items_by_tag_name(self, tag_name):
        declaring_class = self.class_for_tag_name(tag_name)
        return self.get_items_by_class(declaring_class)

    def get_items_by_class(self, cls):
        return [value for value in self._object_register.values() if isinstance(value, cls)]