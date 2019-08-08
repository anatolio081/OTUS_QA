import pytest


@pytest.fixture(scope="session", autouse=True)
def fix_session(request):
    print(f"\n Hello world from '{request.scope}' fixture in conftest.py")

    def fin():
        print(f"\n Bye world from '{request.scope}' fixture in conftest.py")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def fix_module(request):
    print(f"\n fixture begin text from '{request.scope}' in conftest.py")

    def fin():
        print(f"\n fixture END text from '{request.scope}' in conftest.py")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def fix_module_r(request):
    """
    without print in fixture
    """
    return 3


@pytest.fixture(scope="module", params=[1, 3, 5])
def fix_module_w_param_from_confest(request):
    print(f"\n fixture begin text from '{request.scope}' in conftest.py")

    def fin():
        print(f"\n fixture END text from '{request.scope}' in conftest.py")

    request.addfinalizer(fin)
    return request.param


@pytest.fixture(scope="class")
def fix_class(request):
    print(f"\n fixture begin text from '{request.scope}' in conftest.py")

    def fin():
        print(f"\n fixture END text from '{request.scope}' in conftest.py")

    request.addfinalizer(fin)


@pytest.fixture(scope="function")
def fix_func(request):
    print(f"\n fixture begin text from '{request.scope}' in conftest.py")

    def fin():
        print(f"\n fixture END text from '{request.scope}' in conftest.py")

    request.addfinalizer(fin)
