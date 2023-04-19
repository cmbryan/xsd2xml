from pathlib import Path

from lxml import etree

from xsd2xml import xsd_handling

TEST_DATA_DIR = Path(__file__).parent.resolve() / "test_data"

indent_level = 0
result = ""


def start_tag(elt):
    """Example callback function"""
    global indent_level, result
    tag_name = etree.QName(elt).localname  # Strip namespace
    if tag_name == "element":
        result += f"{' ' * indent_level}{tag_name} {elt.get('name').strip()}\n"
    else:
        result += f"{' ' * indent_level}{tag_name}\n"
    indent_level += 1


def end_tag(elt):
    """Example callback function"""
    global indent_level
    indent_level -= 1
    assert indent_level >= 0


def test_process_element():
    """Check that we can load a schema and perform actions on the contents"""
    xsd = etree.parse(TEST_DATA_DIR / "example_schema.xsd")
    xsd_handling.process_element(xsd.getroot(), start_tag, end_tag)

    assert (
        result
        == """schema
 element shiporder
  complexType
   sequence
    element orderperson
    element shipto
     complexType
      sequence
       element name
       element address
       element city
       element country
    element item
     complexType
      sequence
       element title
       element note
       element quantity
       element price
   attribute
"""
    )
