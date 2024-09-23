from collections import defaultdict
from typing import Any

TObj = dict[str, Any]
TListObj = list[TObj]


class TreeStore:
    def __init__(self, items: TListObj) -> None:
        self.dict_items = {i["id"]: i for i in items}
        self.parent_children = self._create_parent_children_list(items)

    @staticmethod
    def _create_parent_children_list(items: TListObj) -> dict[str | int, list[int]]:
        res_dict = defaultdict(list)
        for item in items:
            res_dict[item["parent"]].append(item["id"])

        return res_dict

    def get_all(self) -> TListObj:
        return list(self.dict_items.values())

    def get_item(self, item_id: int) -> TObj:
        item = self.dict_items.get(item_id)
        if item is None:
            print(f"There is no such id: {item_id}")
        return item

    def get_children(self, item_id: int) -> TListObj:
        # без использования вспомогательной хеш-таблицы:
        # [i for i in self.dict_items.values() if i["parent"] == item_id]
        children = self.parent_children.get(item_id) or []
        return [self.dict_items[child_id] for child_id in children]

    def get_all_parents(self, item_id: int) -> TListObj:
        parents = []
        elem_id = item_id
        while True:
            parent_id = self.dict_items[elem_id]["parent"]
            parent_item = self.dict_items.get(parent_id)
            if parent_item is None:
                break
            parents.append(parent_item)
            elem_id = parent_id

        return parents
