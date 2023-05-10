from io import StringIO

from lxml import etree

from tests.test_utils import TEST_DATA_DIR
from xsd2xml import generate


def test_generate():
    """Given the schema, generate an XML file.
    Then validate the output against the schema used to generate it.
    """

    schema = etree.parse(str(TEST_DATA_DIR / "simple_schema_1.xsd"))
    root_element = schema.find("/{http://www.w3.org/2001/XMLSchema}element")

    buffer = StringIO()
    generate.generate_xml(root_element, buffer)
    buffer.seek(0)

    stardard = etree.XMLSchema(schema)
    result = etree.parse(buffer)

    assert stardard.validate(result)
