[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/jsontools.py)

## JSON Flatten/Unflatten

Tools for flatten/unflatten a JSON object.

### `flatten(data, force=False)`

Flattens a JSON object by returning `(Path, Value`) tuples with each path `Path` from root to each value `Value`.

- For each path, if any array with nested dictionary is encountered, the index of the array also becomes part of the path.

- In default, only an array with nested dictionary is flatten. Instead, parameter `force` can be specified to flatten any array.

!!! info
    Different from `dicttools.flatten`, this function accepts any JSON object not limited to dictionary.

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
#  'address.streetAddress': '21 2nd Street',
#  'address.city': 'New York',
#  'phoneNumbers[0].type': 'home',
#  'phoneNumbers[0].number': '212 555-1234',
#  'phoneNumbers[1].type': 'office',
#  'phoneNumbers[1].number': '646 555-4567',
#  'children': [],
#  'spouse': None}
```
