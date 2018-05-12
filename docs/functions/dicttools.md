[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/dicttools.py)

## Dictionary Inverting

Tools for inverting dictionaries.

### `invert(d)`

Inverts `(Key, Value)` pairs to `(Value, Key)`.

- If multiple keys share the same value, the inverted directory keeps last of the respective keys.

### `invert_multiple(d)`

Inverts `(Key, List[Value])` pairs to `(Value, Key)`.

- If multiple keys share the same value, the inverted directory keeps last of the respective keys.

### `invert_safe(d)`

Inverts `(Key, Value)` pairs to `(Value, List[Key])`.

- If multiple keys share the same value, the inverted directory keeps a list of all the respective keys.

## Remapping

Tools for remapping elements.

### `remap(data, mapping, key=None)`

Remaps each unique element in `data` to a new value from calling function `key`.

- `mapping` is a dictionary recording all the mappings, optionally containing previous mappings to reuse.

- In default, `key` returns integers starting from `0`.

``` python
wordmap = {}
db = [list(remap(doc, wordmap)) for doc in docs]
```

## Indexing

Tools for indexing.

### `invertedindex(seqs)`

Creates an [inverted index](https://en.wikipedia.org/wiki/Inverted_index).

- Each item's index is a list of `(ID, position)` pairs for all the sequences in `seqs` containing the item.

``` python
data = [s.split() for s in [
    "a b c d e",
    "b b b d e",
    "c b c c a",
    "b b b c c"
]]

invertedindex(data)
# {'a': [(0, 0), (2, 4)],
#  'b': [(0, 1), (1, 0), (2, 1), (3, 0)],
#  'c': [(0, 2), (2, 0), (3, 3)],
#  'd': [(0, 3), (1, 3)],
#  'e': [(0, 4), (1, 4)]}
```

### `nextentries(data, entries)`

Scans the sequences in `data` from left to right after current entries `entries`, and returns each item and its respective following entries.

- Each entry is a pair of `(ID, Position)` denoting the sequence ID and its respective matching position.

``` python
# same data from previous example

# the first positions of `c` among sequences.
entries = [(0, 2), (2, 0), (3, 3)]

nextentries(data, entries)
# {'d': [(0, 3)],
#  'e': [(0, 4)],
#  'b': [(2, 1)],
#  'c': [(2, 2), (3, 4)],
#  'a': [(2, 4)]}
```

## Dictionary Flatten/Unflatten

Tools for flatten/unflatten a dictionary.

### `flatten(d, force=False)`

Flattens a dictionary by returning `(Path, Value`) tuples with each path `Path` from root to each value `Value`.

- For each path, if any array with nested dictionary is encountered, the index of the array also becomes part of the path.

- In default, only an array with nested dictionary is flatten. Instead, parameter `force` can be specified to flatten any array.

!!! warning
    Different from `jsontools.flatten`, this function accepts only dictionary.

!!! warning
    An empty array disappears after being flatten.

``` python
flatten(json.loads("""{
  "name": "John",
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}"""))
# {'name': 'John',
#  ('address', 'streetAddress'): '21 2nd Street',
#  ('address', 'city'): 'New York',
#  (('phoneNumbers', 0), 'type'): 'home',
#  (('phoneNumbers', 0), 'number'): '212 555-1234',
#  (('phoneNumbers', 1), 'type'): 'office',
#  (('phoneNumbers', 1), 'number'): '646 555-4567',
#  'children': [],
#  'spouse': None}
```

