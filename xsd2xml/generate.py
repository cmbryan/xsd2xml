from io import TextIOBase
from typing import Dict

from lxml.etree import Element, XMLSchema, tostring

from xsd2xml import xsd


def _make_element(template: Dict) -> Element:
    assert len(template) == 1
    elt_name = list(template.keys())[0]
    elt = Element(elt_name)
    for child in template[elt_name]:
        elt.append(_make_element(child))
    return elt


def generate_xml(root_element: XMLSchema, out_stream: TextIOBase):
    xml_template_dict = xsd.create_xsd_dict(root_element)
    xml_doc = _make_element(xml_template_dict)
    out_stream.write(tostring(xml_doc, pretty_print=True).decode())
