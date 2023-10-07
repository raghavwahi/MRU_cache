from src.mru_cache import MRUCache

keys = ["A", "B", "C", "D"]

cache = MRUCache(3)
cache.put("A", {"item": "A"})
cache.put("B", {"item": "B"})
cache.put("C", {"item": "C"})

for key in keys:
    try:
        cache.get(key)
    except KeyError as error:
        print(error)
        continue

print(cache.get_cache())

cache.put("D", {"item": "D"})

for key in keys:
    try:
        cache.get(key)
    except KeyError as error:
        print(error)
        continue

print(cache.get_cache())