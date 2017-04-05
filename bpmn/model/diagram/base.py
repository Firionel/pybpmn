
import inspect

from ..base import BpmnModelObject, BpmnBaseObject


class BpmnDiagramModelObject(BpmnModelObject):

    __child_refs = {'bounds': 'Bounds'}
    __style = {"stroke": "black", "stroke-width": "2px", "fill": "none"}

    def _set_style_on_element(self, element):
        style_string = ''.join(['%s:%s;' % item for item in self._get_style_attributes().items()])
        element.setAttribute("style", style_string)

    def _get_style_attributes(self):
        superclasses = inspect.getmro(self.__class__)
        ret = {}
        for superclass in reversed(superclasses):
            ret.update(getattr(superclass, '_%s__style' % superclass.__name__, {}))
        return ret

    def _create_dom_element(self, document):
        return document.createElement("g")

    def add_to_dom_element(self, element, document):
        new_element = self._create_dom_element(document)
        self._set_style_on_element(new_element)
        self._set_position_information_on_dom_element(new_element)
        element.appendChild(new_element)
        for child in self.children():
            child.add_to_dom_element(new_element, document)

    def _set_position_information_on_dom_element(self, element):
        pass


class BpmnDiagramBaseObject(BpmnDiagramModelObject, BpmnBaseObject):

    __bpmn_attributes = ('bpmnElement', )

    @property
    def referenced_bpmn_element(self):
        return self.definitions.get_item_by_id(self.bpmnElement)


class BpmnLabelledDiagramBaseObject(BpmnDiagramBaseObject):

    __child_refs = {'labels': 'BPMNLabel'}

    def add_to_dom_element(self, element, document):
        super(BpmnLabelledDiagramBaseObject, self).add_to_dom_element(element, document)
        if self.referenced_bpmn_element.name is not None:
            for label in self.labels:
                text_element = document.createElement("text")
                text_node = document.createTextNode(str(self.referenced_bpmn_element.name))
                text_element.appendChild(text_node)
                text_element.setAttribute("transform", "translate(%s, %s)" % (label.x, label.y))
                element.appendChild(text_element)


class BoundedDiagramMixin(object):

    @property
    def bounding_element(self):
        if len(self.bounds) > 0:
            return self.bounds[0]

    @property
    def x(self):
        return self.bounding_element and int(float(self.bounding_element.x))

    @property
    def y(self):
        return self.bounding_element and int(float(self.bounding_element.y))

    @property
    def width(self):
        return self.bounding_element and int(float(self.bounding_element.width))

    @property
    def height(self):
        return self.bounding_element and int(float(self.bounding_element.height))

    def _set_position_information_on_dom_element(self, element):
        if self.bounding_element is not None:
            element.setAttribute("transform", "translate(%d, %d)" % (self.x, self.y))
