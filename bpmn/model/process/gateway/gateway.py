
from ..base import BpmnFlowNode


class BpmnGateway(BpmnFlowNode):

    __tag_names = ('gatewayDirection', )

    def _create_dom_outline(self, document):
        outline_element = document.createElement("rect")
        outline_element.setAttribute("transform", "rotate(45, 18, 18)")
        outline_element.setAttribute("x", "10")
        outline_element.setAttribute("y", "0")
        outline_element.setAttribute("width", "36")
        outline_element.setAttribute("height", "36")
        return outline_element

    def _create_text_dom_element(self, document):
        # gateways are described by labels
        return document.createElement("g")


class BpmnExclusiveGateway(BpmnGateway):

    __tag_names = ('exclusiveGateway', )

    def _create_decorations_element(self, document):
        decorations_element = document.createElement("g")
        decorations_element.setAttribute("style", "fill:black;")
        bar = document.createElement("rect")
        bar.setAttribute("x", "12")
        bar.setAttribute("y", "21.5")
        bar.setAttribute("height", "7")
        bar.setAttribute("width", "28")
        bar.setAttribute("transform", "rotate(45, 26, 25)")
        decorations_element.appendChild(bar)
        second_bar = bar.cloneNode(True)
        second_bar.setAttribute("transform", "rotate(135, 26, 25)")
        decorations_element.appendChild(second_bar)
        return decorations_element


class BpmnInclusiveGateway(BpmnGateway):

    __tag_names = ('inclusiveGateway',)


class BpmnParallelGateway(BpmnGateway):

    __tag_names = ('parallelGateway',)

    def _create_decorations_element(self, document):
        decorations_element = document.createElement("g")
        decorations_element.setAttribute("style", "fill:black;")
        bar = document.createElement("rect")
        bar.setAttribute("x", "12")
        bar.setAttribute("y", "21.5")
        bar.setAttribute("height", "7")
        bar.setAttribute("width", "28")
        bar.setAttribute("transform", "rotate(0, 26, 25)")
        decorations_element.appendChild(bar)
        second_bar = bar.cloneNode(True)
        second_bar.setAttribute("transform", "rotate(90, 26, 25)")
        decorations_element.appendChild(second_bar)
        return decorations_element


class BpmnComplexGateway(BpmnGateway):

    __tag_names = ('complexGateway', )


class BpmnEventBasedGateway(BpmnGateway):

    __tag_names = ('eventBasedGateway', )
    __bpmn_attributes = ('instantiate', 'eventGatewayType')
