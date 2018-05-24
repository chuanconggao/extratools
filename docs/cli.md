# CLI Tools

### `extratools-remap` for [`dicttools.remap`](functions/dicttools.md#remap)

For remapping elements.

- Reads from standard in, and writes to standard out.

- Filename for the mapping dictionary needs to be specified. Loads and dumps as a CSV file.

[Source](https://github.com/chuanconggao/extratools/tree/master/bin/extratools-remap)

``` text
Usage:
    extratools-remap <mapping>
```

### `extratools-flatten` for [`jsontools.flatten`](functions/jsontools.md#flatten)

[Source](https://github.com/chuanconggao/extratools/tree/master/bin/extratools-flatten)

For flatten/unflatten a JSON object.

- Reads from standard in, and writes to standard out.

- `--force` can be specified to force flatten any array.

``` text
Usage:
    extratools-flatten [--force]
```

### `extratools-teststats` for [`stattools.teststats`](functions/stattools.md#teststats)

[Source](https://github.com/chuanconggao/extratools/tree/master/bin/extratools-teststats)

For evaluating binary classification results.

- Reads two files for truths and predictions, respectively. Each row is a label denoting true or false.

- Writes all the statistics to standard out in JSON.

``` text
Usage:
    extratools-teststats <truth> <prediction>
```
