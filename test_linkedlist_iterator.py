import pytest
try:
    from linkedlist_iterator import LinkedList
except:
    from .linkedlist_iterator import LinkedList


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_len_ll():
    ll = LinkedList(["Monday", "Tuesday", "Wednesday"])

    assert len(ll) == 3

# @pytest.mark.skip("TODO")
def test_eqality_ll():
    ll = LinkedList(["Monday", "Tuesday", "Wednesday"])

    assert ll == ["Monday", "Tuesday", "Wednesday"]

# @pytest.mark.skip("TODO")
def test_first_element_ll():
    ll = LinkedList(["Monday", "Tuesday", "Wednesday"])

    assert list(ll)[0] == "Monday"