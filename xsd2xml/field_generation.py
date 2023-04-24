def generate_field(data_type):
    """Given a datatype, generate a valid instance.

    Will be extended in the future to generate realistic data using the datatype and a
    supplied configuration file.
    """
    if data_type == str:
        return "AAA"
    elif data_type == int:
        return 7
    else:
        raise NotImplementedError(f"Cannot generate data for the {data_type} type.")
