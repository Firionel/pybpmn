
import xml.dom.minidom as dom


class BpmnDiagramSvgExporter(object):

    def __init__(self, diagram):
        self._diagram = diagram

    def export(self, filename):
        svg_document = dom.getDOMImplementation().createDocument(None, "svg", None)
        self._diagram.write_to_document(svg_document)
        with open(filename, 'w') as f:
            f.write(svg_document.toprettyxml())
