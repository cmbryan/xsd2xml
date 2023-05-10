from argparse import ArgumentParser, Namespace
from pathlib import Path

from lxml import etree

import xsd2xml
from tests.test_utils import TEST_DATA_DIR
from xsd2xml.__main__ import main


def test_version():
    assert xsd2xml.__version__ == "0.1.0"


def test_main(tmp_path: Path):
    """Really an end2end test"""
    args = Namespace(
        xsd=str(TEST_DATA_DIR / "simple_schema_1.xsd"),
        # constraints=None,
        xml=str(tmp_path / "out.xml"),
    )

    main(args)

    schema = etree.XMLSchema(etree.parse(args.xsd))
    output = etree.parse(args.xml)
    assert schema.validate(output)
