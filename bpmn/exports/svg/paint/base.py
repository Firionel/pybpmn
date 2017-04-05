
import inspect

from ....util.reflection import get_all_subclasses_for_class
from ....util.format import format_text_svg


class ProcessElementSvgPainter(object):

    def __init__(self, process_element):
        self._process_element = process_element

    @classmethod
    def for_bpmn_element(cls, bpmn_element):

        for element_cls in inspect.getmro(bpmn_element.__class__):
            for painter_cls in get_all_subclasses_for_class(cls):
                if element_cls.__name__ in getattr(painter_cls, '_%s__process_classes' % painter_cls.__name__, tuple):
                    break
        else:
            raise RuntimeError("No painter class found for bpmn element class %s." % element_cls.__name__)

        return element_cls(bpmn_element)

    def _create_text_dom_element(self, document):

        text_element = format_text_svg(document, str(self.name), 13)
        text_element.setAttribute("x", "20")
        text_element.setAttribute("y", "20")
        text_element.setAttribute("width", "40")
        text_element.setAttribute("height", "55")
        for tspan in text_element.getElementsByTagName("tspan"):
            tspan.setAttribute("x", text_element.getAttribute("x"))
        return text_element

    def create_dom_shape(self, document):
        group_element = document.createElement("g")
        shape_element = self._create_dom_outline(document)
        text_element = self._create_text_dom_element(document)
        decorations_element = self._create_decorations_element(document)
        group_element.appendChild(shape_element)
        group_element.appendChild(text_element)
        group_element.appendChild(decorations_element)
        return group_element

    def _create_dom_outline(self, document):
        return document.createElement("g")

    def _create_decorations_element(self, document):
        return document.createElement("g")
