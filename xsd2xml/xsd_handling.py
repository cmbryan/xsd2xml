def process_element(elt, start_elt_cb, end_elt_cb):
    """Given an XML element from a schema, act on its contents and traverse into it's children"""
    start_elt_cb(elt)
    for child in elt:
        # recursive
        process_element(child, start_elt_cb, end_elt_cb)
    end_elt_cb(elt)
