
# Brandon Jun // COMSC 078 // Trees & Dictionaries

def tree(label, branches=[]):

    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


def label(t):
    return t[0]


def branches(t):
    return t[1:]


def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_tree(branch):
            return False
    return True


def is_leaf(t):
    return not branches(t)


def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])


def main():

    t = tree(4, [tree(2, [tree(1), tree(3)]),
                 tree(6, [tree(5)])])

    print("Tree:", t)
    print("Label:", label(t))
    print("Branches:", branches(t))
    print("Number of leaves:", count_leaves(t))


main()

