
from bpmn.model.base import BpmnModelObject
from bpmn.model.definitions import BpmnDefinitions

from xml.dom.minidom import parse


class BpmnFileImporter(object):

    def __init__(self, filename):
        self._filename = filename

    def run_import(self):
        dom = parse(self._filename)
        definitions_element = dom.getElementsByTagName('bpmn:definitions')[0]
        return BpmnDefinitions.from_dom_node(None, definitions_element)
