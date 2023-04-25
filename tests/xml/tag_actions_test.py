from lxml import etree

from tests.test_utils import TEST_DATA_DIR
from xsd2xml.xml import tag_actions, utils

indent_level = 0
result = ""


def __start_tag(elt):
    """Example callback function"""
    global indent_level, result
    name = utils.tag_name(elt)  # Strip namespace
    if name == "element":
        result += f"{' ' * indent_level}{name} {elt.get('name').strip()}\n"
    else:
        result += f"{' ' * indent_level}{name}\n"
    indent_level += 1


def __end_tag(elt):
    """Example callback function"""
    global indent_level
    indent_level -= 1
    assert indent_level >= 0


def test_process_element():
    """Check that we can load a schema and perform actions on the contents"""
    xsd = etree.parse(TEST_DATA_DIR / "example_schema.xsd")
    tag_actions.process_tag(xsd.getroot(), __start_tag, __end_tag)

    assert (
        result
        == """element shiporder
 element orderperson
 element shipto
  element name
  element address
  element city
  element country
 element item
  element title
  element note
  element quantity
  element price
"""
    )
