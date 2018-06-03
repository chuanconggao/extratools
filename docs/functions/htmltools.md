[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/htmltools.py)

## Generating HTML

Tools for generating HTML snippets.

### `emmet`

`emmet(abbr)` generates the HTML snippet according to abbreviation `abbr` in [Emmet](https://docs.emmet.io/abbreviations/) syntax.

!!! danger
    [Node.js](https://nodejs.org/) and [NPM](https://www.npmjs.com/) must be properly installed and accessible on `PATH`.

!!! warning
    When calling for the first time, proper Node.js dependencies will be installed, with the following message `Installing Node.js dependencies...` printed to standard error.

!!! info
    This function is a wrapper of the official Node.js package [@emmetio/expand-abbreviation](https://www.npmjs.com/package/@emmetio/expand-abbreviation).

``` python
print(emmet("ul.nav>.nav-item{Item $}*2"))
# <ul class="nav">
# 	<li class="nav-item">Item 1</li>
# 	<li class="nav-item">Item 2</li>
# </ul>
```
