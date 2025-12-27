import pytest

# Toggle test files on/off by setting value to True/False
TEST_FILES = {
    # "tests/test_login.py": True,
    "tests/test_sales_order.py": True,
}


def main():
    selected = [path for path, enabled in TEST_FILES.items() if enabled]
    if not selected:
        raise SystemExit("No tests enabled in TEST_FILES.")
    raise SystemExit(pytest.main(["-v", *selected]))


if __name__ == "__main__":
    main()

