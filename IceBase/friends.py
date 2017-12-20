#!/usr/bin/python
# -*- coding: utf-8 -*-

class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if not connection in self.connections:
            self.connections.append(connection)
            return True
        return False

    def remove(self, connection):
        try:
            self.connections.remove(connection)
            return True
        except:
            return False

    def names(self):        
        return set([n for c in self.connections for n in c ])

    def connected(self, name):
        name_connection = set([n for c in self.connections for n in c if name in c])
        if name in name_connection:
            name_connection.remove(name)
        return name_connection 


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"


