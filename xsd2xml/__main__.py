import argparse

# import tomli
from lxml import etree

from xsd2xml.generate import generate_xml


def main(args):
    xsd = etree.parse(args.xsd)
    # if args.constraints:
    #     with open(args.constraints) as constraints_fh:
    #         constraints = tomli.load(constraints_fh)
    #         print(f"todo, process {str(constraints)}")

    with open(args.xml, "w") as xml_fh:
        generate_xml(
            root_element=xsd.find("/{http://www.w3.org/2001/XMLSchema}element"),
            out_stream=xml_fh,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""A Python module that generates XML matching an XSD and (o\
                   ptionally) regex constraints for the value of each tag."""
    )
    parser.add_argument("--xsd", help="XML Schema", required=True)
    # parser.add_argument("--constraints", nargs="?")
    parser.add_argument("--xml", help="Output XML path", required=True)

    args = parser.parse_args()
    main(args)
