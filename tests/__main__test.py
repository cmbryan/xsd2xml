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
        xsd=str(TEST_DATA_DIR / "example_schema.xsd"),
        constraints=None,
        xml=str(tmp_path / "out.xml"),
    )

    main(args)

    # pick up here by examining args.xml
    doc = etree.parse(args.xml)
    assert 0
