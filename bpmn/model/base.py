
import inspect
import uuid
from weakref import ref
from xml.dom.minidom import Node

from .exceptions import NoResponsibleClass, ResponsibleClassAmbiguous
from ..util.reflection import get_all_subclasses_for_class


class BpmnModelObject(object):

    __tag_names = tuple()
    __bpmn_attributes = tuple()
    _child_refs = {}
    _class_cache = {}
    requires_id = False

    def __init__(self, definitions_parent):
        self._synthetic_id = uuid.uuid4().get_hex()
        self._definitions = definitions_parent
        for attribute_name in self.get_bpmn_attributes():
            if not hasattr(self, attribute_name) and attribute_name != 'id':
                setattr(self, attribute_name, None)
        self._definitions.register(self)
        self._children = []


    @property
    def access_id(self):
        return self._synthetic_id

    @property
    def definitions(self):
        return self._definitions

    @classmethod
    def class_for_tag_name(cls, tag_name):
        tag_name = tag_name.split(':')[-1] # TODO: hack for namespace
        if tag_name in cls._class_cache:
            return cls._class_cache[tag_name]

        declaring_classes = [c for c in get_all_subclasses_for_class(cls) if
                             tag_name in getattr(c, '_%s__tag_names' % c.__name__, tuple())]
        leaf_classes = [c for c in declaring_classes if not
                        [d for d in declaring_classes if d != c and issubclass(d, c)]]

        if not leaf_classes:
            raise NoResponsibleClass("No responsible class found for tag name '%s'." % (tag_name,))

        if len(leaf_classes) > 1:
            raise ResponsibleClassAmbiguous("Responsible class for tag name '%s' is ambiguous." % (tag_name,))

        target_class = leaf_classes[0]
        cls._class_cache[tag_name] = target_class
        return target_class

    @classmethod
    def get_bpmn_attributes(cls):
        superclasses = inspect.getmro(cls)
        ret = set()
        for superclass in superclasses:
            ret = ret.union(set(getattr(superclass, '_%s__bpmn_attributes' % superclass.__name__, set())))
        return ret

    @classmethod
    def get_child_references(cls):
        superclasses = inspect.getmro(cls)
        ret = {}
        for superclass in superclasses:
            ret.update(getattr(superclass, '_%s__child_refs' % superclass.__name__, dict()))
        return ret

    @staticmethod
    def _element_id_from_node(node):
        return node.attributes["id"].value

    @classmethod
    def _set_attributes_from_node(cls, node, instance):
        for attribute_name in cls.get_bpmn_attributes():
            if attribute_name == 'id':
                continue
            if node.hasAttribute(attribute_name):
                attribute_value = node.getAttribute(attribute_name)
                setattr(instance, attribute_name, attribute_value)

    @classmethod
    def from_dom_node(cls, parent_definitions, node):
        target_class = cls.class_for_tag_name(node.tagName)
        if target_class.requires_id:
            element_id = cls._element_id_from_node(node)
            instance = target_class(element_id, parent_definitions)
        else:
            instance = target_class(parent_definitions)
        target_class._set_attributes_from_node(node, instance)
        target_child_references = target_class.get_child_references()
        for child_node in node.childNodes:
            if child_node.nodeType != Node.ELEMENT_NODE:
                continue
            try:
                child_instance = BpmnModelObject.from_dom_node(parent_definitions, child_node)
                instance._children.append(ref(child_instance))
            except NoResponsibleClass:
                pass
            except  ResponsibleClassAmbiguous:
                pass

        return instance

    def __repr__(self):
        if hasattr(self, 'name'):
            return '<%s %s (@ %s)>' % (self.__class__.__name__, self.name, id(self))
        else:
            return '<%s (@ %s)>' % (self.__class__.__name__, id(self))

    def children(self, reftype=None):
        if reftype is None:
            return [value for value in [r() for r in self._children] if value is not None]
        else:
            child_refs = self.get_child_references()
            matching_class = self.__class__.class_for_tag_name(child_refs[reftype])
            return [child for child in self.children() if isinstance(child, matching_class)]


class BpmnBaseObject(BpmnModelObject):
    __bpmn_attributes = ('id',)
    __child_refs = {'documentations': 'documentation'}
    requires_id = True

    def __init__(self, element_id, parent_definitions):
        self._id = element_id
        super(BpmnBaseObject, self).__init__(parent_definitions)

    @property
    def id(self):
        return self._id

    @property
    def access_id(self):
        return self.id

    def __repr__(self):
        if hasattr(self, 'name'):
            return '<%s %s (id: %s)>' % (self.__class__.__name__, self.name, self.id)
        else:
            return '<%s (id: %s)>' % (self.__class__.__name__, self.id)