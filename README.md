# MRU_Cache

MRU_Cache is a Python project that implements a Most Recently Used (MRU) cache using a doubly linked list. This project consists of three main components:

1. DoublyLinkedList: A custom doubly linked list class that is used as the underlying data structure for managing the cache items.
2. Node: A class representing individual nodes in the doubly linked list.
3. MRUCache: A class that implements the MRU cache using the provided doubly linked list.

## Usage

### DoublyLinkedList

The `DoublyLinkedList` class provides the foundation for your MRUCache. It allows you to manipulate the linked list, including operations such as inserting at the head, removing a specific node, and more. You can use it as follows:

```python
from src.doubly_linked_list import DoublyLinkedList

# Create a new linked list
my_list = DoublyLinkedList()

# Insert a new node at the tail
my_list.append(data)

# Insert a new node at the head
my_list.insert_at_head(data)

# Remove a node from the tail
value = my_list.pop()

# Remove a specific node based on value
my_list.remove(value)

# Remove a node from the head
value = my_list.remove_from_head()

# Get header
header = my_list.get_header()

# get current doubly linked list
complete_list = my_list.get_list()
```

### Node

The `Node` class represents individual nodes in the doubly linked list. Each node contains a data element and references to the previous and next nodes in the list. You can use it as follows:

```python
from src.doubly_linked_list import Node

# Create a new node
my_node = Node(data)

# Update next node
my_node.update_next(node)

# Update previous node
my_node.update_previous(node)

# Access node data
data = my_node.value

# Access previous and next nodes
prev_node = my_node.previous_node
next_node = my_node.next_node
```

### MRUCache

The `MRUCache` class utilizes the doubly linked list to create an MRU cache with a specified capacity. It provides methods for inserting, retrieving, and removing items from the cache while maintaining the MRU eviction policy. You can use it as follows:

```python
from src.mru_cache import MRUCache

# Create a new MRU cache with a specified capacity
my_cache = MRUCache(capacity)

# Insert an item into the cache
my_cache.put(key, value)

# Retrieve an item from the cache
value = my_cache.get(key)

# Retrieve current cache
data = my_cache.get_cache()
```

## Example

Here's a simple example of how to use the MRUCache class:

```python
# Import the MRUCache class
from src.mru_cache import MRUCache

# Create an MRU cache with a capacity of 3
cache = MRUCache(3)

# Insert items into the cache
cache.put("A", {"item": 1})
cache.put("B", {"item": 2})
cache.put("C", {"item": 3})

# Retrieve items from the cache
print(cache.get("A"))  # Output {"item": 1}
print(cache.get("B"))  # Output {"item": 1}

# Insert a new item, causing the least recently used item ("C") to be evicted
cache.put("D", {"item": 4})
print(cache.get("C"))  # Output: Error as C was evicted
```

## Contributing

Contributions to the MRUCache project are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear commit messages.
4. Create a pull request to merge your changes into the main branch.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE License. See the [LICENCE](LICENSE) file for details.

---

Feel free to customize this `README.md` file with additional information about your project, such as installation instructions, testing procedures, and more.