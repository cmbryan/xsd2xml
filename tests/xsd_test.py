import random

from lxml import etree

from tests.test_utils import TEST_DATA_DIR
from xsd2xml import xsd


def test_create_xsd_dict():
    random.seed(1)  # determinism

    s = etree.parse(str(TEST_DATA_DIR / "simple_schema_1.xsd"))
    root_element = s.find("/{http://www.w3.org/2001/XMLSchema}element")
    assert xsd.create_xsd_dict(root_element) == {
        "note": [
            {"to": []},
            {"from": []},
            {"heading": []},
            {"body": []},
            {"apple": []},
        ]
    }
