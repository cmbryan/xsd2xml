from xsd2xml.xml_utils import tag_name


def process_tag(elt, start_elt_cb, end_elt_cb):
    """Given an XML element from a schema, act on its contents and traverse into its
    children
    """

    name = tag_name(elt)
    if name == "element":
        start_elt_cb(elt)

    for child in elt:
        # recursive
        process_tag(child, start_elt_cb, end_elt_cb)

    if name == "element":
        end_elt_cb(elt)
