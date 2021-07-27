class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 3을 가진 Node 를 만드려면 아래와 같이 하면 됩니다!
node = Node(3) # 현재는 next 가 없이 하나의 노드만 있습니다. [3]
print(node.data)