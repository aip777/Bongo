
class Tree:
    def __init__(self, key):
        self.key = key
        self.leftNode = None
        self.rightNode = None

def searchPath(foundation, path, arg):
    if foundation is None:
        return False
    path.append(foundation.key)
    if foundation.key == arg:
        return True

    if ((foundation.leftNode != None and searchPath(foundation.leftNode, path, arg)) or
            (foundation.rightNode != None and searchPath(foundation.rightNode, path, arg))):
        return True
    path.pop()
    return False

def lca(foundation, node1, node2):
    path1 = []
    path2 = []
    if (not searchPath(foundation, path1, node1) or not searchPath(foundation, path2, node2)):
        return -1
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]
foundation = Tree(1)
foundation.leftNode = Tree(2)
foundation.rightNode = Tree(3)
foundation.leftNode.leftNode = Tree(4)
foundation.leftNode.rightNode = Tree(5)
foundation.rightNode.leftNode = Tree(6)
foundation.rightNode.rightNode = Tree(7)
print ("6, 7 = %d" % (lca(foundation, 6, 7)))
print ("3, 7 = %d" % (lca(foundation, 3, 7)))

first_number = int(input("Enter Your First Number: "))
second_number = int(input("Enter Your Second Number: "))
print (first_number, ',', second_number," = %d" % (lca(foundation, first_number, second_number)))
