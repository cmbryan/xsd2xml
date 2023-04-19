import argparse

import tomli
from lxml import etree


def main(args):
    xsd = etree.parse(args.xsd)
    if args.constraints:
        with open(args.constraints) as constraints_fh:
            constraints = tomli.load(constraints_fh)
            print(f"todo, process {str(constraints)}")

    print(f"todo, process {xsd.getroot().tag}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""A Python module that generates XML matching an XSD and (o\
                   ptionally) regex constraints for the value of each tag."""
    )
    parser.add_argument("--xsd", help="XML Schema", required=True)
    parser.add_argument("--constraints", nargs="?")

    args = parser.parse_args()
    main(args)
