import pytest
from tree_store.tree_store import TreeStore


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None},
]


@pytest.fixture
def tree_store():
    return TreeStore(items)


def test_get_all(tree_store):
    assert tree_store.get_all() == items


def test_get_item(tree_store):
    assert tree_store.get_item(7) == {"id": 7, "parent": 4, "type": None}


def test_get_parents(tree_store):
    assert tree_store.get_all_parents(7) == [
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 1, "parent": "root"},
    ]


def test_get_children(tree_store):
    assert tree_store.get_children(4) == [
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None},
    ]


def test_get_without_children(tree_store):
    assert tree_store.get_children(5) == []
