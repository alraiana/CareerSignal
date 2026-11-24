from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")


def test_app_renders_title():
    at = AppTest.from_file(APP_PATH).run()
    assert not at.exception
    assert at.title[0].value == "CareerSignal"
