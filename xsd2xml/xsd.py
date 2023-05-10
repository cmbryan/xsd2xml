from random import choice
from typing import Dict

from lxml import etree

ns_map = {
    "xs": "{http://www.w3.org/2001/XMLSchema}",
}


def create_xsd_dict(elt: etree.Element) -> Dict:
    """Return a dictionary containing XML elements to create.

    (Not concerned with tag content yet, only structure.)
    """

    if elt.tag == f"{ns_map['xs']}complexType":
        return create_xsd_dict(elt[0])

    elif elt.tag == f"{ns_map['xs']}sequence":
        return [create_xsd_dict(ch) for ch in elt]

    elif elt.tag == f"{ns_map['xs']}choice":
        return [create_xsd_dict(choice(elt))]

    elif elt.tag == f"{ns_map['xs']}element":
        return {elt.get("name"): [create_xsd_dict(ch) for ch in elt]}

    else:
        assert False  # TODO
