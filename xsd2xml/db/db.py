import sqlite3
import tempfile
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def xml_db():
    # Create temp database
    with tempfile.TemporaryDirectory() as dir, open(
        Path(__file__).parent / "model.sql"
    ) as fh:
        db = sqlite3.connect(Path(dir) / "xml_db.sqlite3")
        db.executescript(fh.read())

        yield db
