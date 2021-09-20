import pytest


def always_returns_true():
    return False
    print('turtle')

def test_always_returns_true():
    assert always_returns_true()
