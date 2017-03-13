
from cStringIO import StringIO

from ..base import BpmnBaseObject


class BpmnDiagram(BpmnBaseObject):

    __tag_names = ('BPMNDiagram', )
    __child_refs = {'planes': 'BPMNPlane'}


    def write_svg(self, path):
        output = StringIO()
        output.write(self._get_svg_header())
        for child in self.children():
            output.write(child.svg_string())
        output.write(self._write_svg_closer())
