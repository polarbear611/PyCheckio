#!/usr/bin/python
# -*- coding: utf-8 -*-

def is_family(tree):
    family_tree = []
    ancestor = set([e[0] for e in tree if e[0] not in [e[1] for e in tree]])
    if len(ancestor) != 1:
        return False
    father = [ancestor.pop()]
    family_tree.append(father[0])
    while(tree and father):
        for f in father[:]:
            for e in tree[:]:
                if f == e[0] and e[1] not in family_tree:
                    father.append(e[1])
                    family_tree.append(e[1])
                    tree.remove(e)
            father.remove(f)
    return not tree

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")

