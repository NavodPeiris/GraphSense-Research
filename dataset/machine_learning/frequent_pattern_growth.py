
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TreeNode:

    name: str
    count: int
    parent: TreeNode | None = None
    children: dict[str, TreeNode] = field(default_factory=dict)
    node_link: TreeNode | None = None

    def __repr__(self) -> str:
        return f"TreeNode({self.name!r}, {self.count!r}, {self.parent!r})"

    def inc(self, num_occur: int) -> None:
        self.count += num_occur

    def disp(self, ind: int = 1) -> None:
        print(f"{'  ' * ind} {self.name}  {self.count}")
        for child in self.children.values():
            child.disp(ind + 1)


def create_tree(data_set: list, min_sup: int = 1) -> tuple[TreeNode, dict]:
    header_table: dict = {}
    for trans in data_set:
        for item in trans:
            header_table[item] = header_table.get(item, [0, None])
            header_table[item][0] += 1

    for k in list(header_table):
        if header_table[k][0] < min_sup:
            del header_table[k]

    if not (freq_item_set := set(header_table)):
        return TreeNode("Null Set", 1, None), {}

    for key, value in header_table.items():
        header_table[key] = [value, None]

    fp_tree = TreeNode("Null Set", 1, None)  
    for tran_set in data_set:
        local_d = {
            item: header_table[item][0] for item in tran_set if item in freq_item_set
        }
        if local_d:
            sorted_items = sorted(
                local_d.items(), key=lambda item_info: item_info[1], reverse=True
            )
            ordered_items = [item[0] for item in sorted_items]
            update_tree(ordered_items, fp_tree, header_table, 1)

    return fp_tree, header_table


def update_tree(items: list, in_tree: TreeNode, header_table: dict, count: int) -> None:
    if items[0] in in_tree.children:
        in_tree.children[items[0]].inc(count)
    else:
        in_tree.children[items[0]] = TreeNode(items[0], count, in_tree)
        if header_table[items[0]][1] is None:
            header_table[items[0]][1] = in_tree.children[items[0]]
        else:
            update_header(header_table[items[0]][1], in_tree.children[items[0]])
    if len(items) > 1:
        update_tree(items[1:], in_tree.children[items[0]], header_table, count)


def update_header(node_to_test: TreeNode, target_node: TreeNode) -> TreeNode:
    while node_to_test.node_link is not None:
        node_to_test = node_to_test.node_link
    if node_to_test.node_link is None:
        node_to_test.node_link = target_node
    
    return node_to_test


def ascend_tree(leaf_node: TreeNode, prefix_path: list[str]) -> None:
    if leaf_node.parent is not None:
        prefix_path.append(leaf_node.name)
        ascend_tree(leaf_node.parent, prefix_path)


def find_prefix_path(base_pat: frozenset, tree_node: TreeNode | None) -> dict:  
    cond_pats: dict = {}
    while tree_node is not None:
        prefix_path: list = []
        ascend_tree(tree_node, prefix_path)
        if len(prefix_path) > 1:
            cond_pats[frozenset(prefix_path[1:])] = tree_node.count
        tree_node = tree_node.node_link
    return cond_pats


def mine_tree(
    in_tree: TreeNode,  
    header_table: dict,
    min_sup: int,
    pre_fix: set,
    freq_item_list: list,
) -> None:
    sorted_items = sorted(header_table.items(), key=lambda item_info: item_info[1][0])
    big_l = [item[0] for item in sorted_items]
    for base_pat in big_l:
        new_freq_set = pre_fix.copy()
        new_freq_set.add(base_pat)
        freq_item_list.append(new_freq_set)
        cond_patt_bases = find_prefix_path(base_pat, header_table[base_pat][1])
        my_cond_tree, my_head = create_tree(list(cond_patt_bases), min_sup)
        if my_head is not None:
            
            header_table[base_pat][1] = update_header(
                header_table[base_pat][1], my_cond_tree
            )
            mine_tree(my_cond_tree, my_head, min_sup, new_freq_set, freq_item_list)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    data_set: list[frozenset] = [
        frozenset(["bread", "milk", "cheese"]),
        frozenset(["bread", "milk"]),
        frozenset(["bread", "diapers"]),
        frozenset(["bread", "milk", "diapers"]),
        frozenset(["milk", "diapers"]),
        frozenset(["milk", "cheese"]),
        frozenset(["diapers", "cheese"]),
        frozenset(["bread", "milk", "cheese", "diapers"]),
    ]
    print(f"{len(data_set) = }")
    fp_tree, header_table = create_tree(data_set, min_sup=3)
    print(f"{fp_tree = }")
    print(f"{len(header_table) = }")
    freq_items: list = []
    mine_tree(fp_tree, header_table, 3, set(), freq_items)
    print(f"{freq_items = }")
