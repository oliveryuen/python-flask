import pytest

from myflaskapp import create_app


@pytest.fixture(scope="session")
def client(request):
    app = create_app()
    return app.test_client()
