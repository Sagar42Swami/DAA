import heapq

# Node structure for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison for priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq

# Function to generate Huffman Codes
def generate_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

# Huffman Encoding main function
def huffman_encoding(chars, freqs):
    heap = []
    # Step 1: Build a min-heap
    for i in range(len(chars)):
        heapq.heappush(heap, Node(chars[i], freqs[i]))

    # Step 2: Merge nodes until one root remains
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # Step 3: Generate Huffman Codes
    root = heap[0]
    codes = {}
    generate_codes(root, "", codes)
    return codes

# Example usage
if __name__ == "__main__":
    chars = ['A', 'B', 'C', 'D', 'E']
    freqs = [5, 9, 12, 13, 16]
    codes = huffman_encoding(chars, freqs)
    print("Huffman Codes:")
    for char, code in codes.items():
        print(f"{char}: {code}")

'''
                  (55)
                /    \
            (25)      (30)
           /   \      /   \
        C(12) D(13) (14)  E(16)
                   /   \
                A(5)  B(9)
                
                | Character | Path                         | Code    |
| --------- | ---------------------------- | ------- |
| C         | Left → Left → `00`           | **00**  |
| D         | Left → Right → `01`          | **01**  |
| A         | Right → Left → Left → `100`  | **100** |
| B         | Right → Left → Right → `101` | **101** |
| E         | Right → Right → `11`         | **11**  |

'''