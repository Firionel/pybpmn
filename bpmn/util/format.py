
import re


def format_text_svg(document, text, maximum_col_width):
    line_height = 12

    text_element = document.createElement("text")
    text_passages = re.split(r"\s", text)
    if len(text_passages) == 0:
        # nothing to do
        pass
    elif len(text_passages) == 1:
        tspan_element = document.createElement("tspan")
        text_element.appendChild(tspan_element)
        data_node = document.createTextNode(text_passages[0])
        text_element.appendChild(data_node)
    else:
        this_passage = text_passages.pop(0)
        while text_passages:
            next_passage = text_passages.pop(0)
            if len(this_passage) + len(next_passage) + 1 > maximum_col_width:
                tspan_element = document.createElement("tspan")
                tspan_element.setAttribute("dy", str(line_height))
                text_element.appendChild(tspan_element)
                data_node = document.createTextNode(this_passage)
                text_element.appendChild(data_node)
                this_passage = next_passage
            else:
                this_passage = ' '.join((this_passage, next_passage))
        else:
            tspan_element = document.createElement("tspan")
            tspan_element.setAttribute("dy", str(line_height))
            text_element.appendChild(tspan_element)
            data_node = document.createTextNode(this_passage)
            text_element.appendChild(data_node)

    return text_element
