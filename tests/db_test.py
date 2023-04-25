from xsd2xml import db


def test_db():
    with db.xml_db() as conn:
        conn.execute(
            """
            insert into Namespace(
                prefix_name,
                url
            ) values (
                "pfix",
                "http://test"
            );
            """
        )
