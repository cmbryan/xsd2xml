from xsd2xml import field_generation


def test_generate_field():
    assert field_generation.generate_field(str) == "AAA"
