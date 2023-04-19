# Test the example code in the README.md

import tomli


def test_constraints():
    input = r"""
[constraints]

# XPath = Regex
email = '^\S+@\S+\.\S+$'
"fruit/apple" = "golden_delicious|honey_crisp"
"""

    constraints = tomli.loads(input)
    assert {
        "constraints": {
            "email": "^\\S+@\\S+\\.\\S+$",
            "fruit/apple": "golden_delicious|honey_crisp",
        }
    } == constraints
