from lxml import etree


def tag_name(tag):
    """return the name of the XML tag without namespace"""
    return etree.QName(tag).localname
