# conftest.py next to the HIL tests: adds the --port option to pytest.
def pytest_addoption(parser):
    parser.addoption("--port", action="store", default="COM5", help="serial port of the board")
