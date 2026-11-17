
import heapq

# Node class
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Characters and frequencies
chars = ['A', 'B', 'C', 'D', 'E', 'F']
freq = [5, 9, 12, 13, 16, 45]

heap = []

# Insert all characters into min heap
for i in range(len(chars)):
    node = Node(chars[i], freq[i])
    heapq.heappush(heap, (freq[i], i, node))

count = len(chars)

# Build Huffman Tree
while len(heap) > 1:

    f1, _, left = heapq.heappop(heap)
    f2, _, right = heapq.heappop(heap)

    new_node = Node(None, f1 + f2)
    new_node.left = left
    new_node.right = right

    heapq.heappush(heap, (f1 + f2, count, new_node))
    count = count + 1

# Generate Huffman Codes
def generate_codes(root, code):

    if root.char is not None:
        print(root.char, ":", code)
        return

    generate_codes(root.left, code + "0")
    generate_codes(root.right, code + "1")

root = heap[0][2]

print("Huffman Codes:")
generate_codes(root, "")
