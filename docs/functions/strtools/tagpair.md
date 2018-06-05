Tools for matching pair of tags.

!!! warning
    Functions below assume the tags are well balanced. May work for certain unbalanced scenarios without guarantee.

    When the open tag and the close tag are identical, there is no nested tag structure.

!!! info
    Functions below use similar arguments.

    - `tag` specifies the open tag, while `closetag` specifies the close tag. If `closetag` is unspecified, the open tag and the close tag are assumed to be identical.

    - `useregex` specifies whether to use regular expression for `tag` and `closetag`, and defaults to `False`.

## Finding Pair of Tags

Tools for finding pair of tags.

### `findtagpairspans`

`findtagpairspans(s, tag, closetag=None, useregex=False)` finds the position span of each pair of tags in string `s`.


``` python
# |--| denotes each span.

list(findtagpairspans("a$b$c$$d#ef#g", r"\$|#", useregex=True))
# [(1, 4),              |-|
#  (5, 7),                  ||
#  (8, 12)]                    |--|

list(findtagpairspans("a(b(c()d)ef)g", '(', ')'))
# [(5, 7),                  ||
#  (3, 9),                |----|
#  (1, 12)]             |---------|

list(findtagpairspans("a<a>b<b>c<c></c>d</b>ef</a>g", r"<\w+>", r"</\w+>", useregex=True))
# [(9, 16),                     |-----|
#  (5, 21),                 |--------------|
#  (1, 27)]             |------------------------|
```

### `findtagpair`

`findtagpair(s, pos, tag, closetag=None, useregex=False)` finds the pair of tags covering the specified position `pos` in string `s`. Returns `None` if there is no covering pair of tags.

``` python
# | denotes each specified position.

#                |
findtagpair("a$b$c$$d#ef#g", 4, r"\$|#", useregex=True)
# None

#                  |
findtagpair("a$b$c$$d#ef#g", 6, r"\$|#", useregex=True)
#                '$$'

#                |
findtagpair("a(b(c()d)ef)g", 4, '(', ')')
#              '(c()d)'

#                  |
findtagpair("a(b(c()d)ef)g", 6, '(', ')')
#                '()'

#                    |
findtagpair("a<a>b<b>c<c></c>d</b>ef</a>g", 8, r"<\w+>", r"</\w+>", useregex=True)
#                '<b>c<c></c>d</b>'

#                      |
findtagpair("a<a>b<b>c<c></c>d</b>ef</a>g", 10, r"<\w+>", r"</\w+>", useregex=True)
#                    '<c></c>'
```

### `findmatchingtag`

`findmatchingtag(s, pos, tag, closetag=None, useregex=False)` finds the other matching tag of the current tag at the specified position `pos` in string `s`. Returns `None` if there is no covering pair of tags.

- If there is no tag at the specified position, returns the open tag.

!!! tip
    The behavior of this function is designed to mimic Vim's [`%` operation](http://vimdoc.sourceforge.net/htmldoc/motion.html#%).

``` python
# | denotes each specified position.
# == denotes the other matching tag.

#                      |
findmatchingtag("a$b$c$$d#ef#g", 6, r"\$|#", useregex=True)
#                     =
# (5, 6)             '$$'

#                    |
findmatchingtag("a(b(c()d)ef)g", 4, '(', ')')
#                   =
# (3, 4)           '(c()d)'

#                      |
findmatchingtag("a<a>b<b>c<c></c>d</b>ef</a>g", 6, r"<\w+>", r"</\w+>", useregex=True)
#                                 ====
# (17, 21)           '<b>c<c></c>d</b>'
```

## Updating Pair of Tags

Tools for updating pair of tags.

### `addtagpair`

`addtagpair(s, pos, tag, closetag=None, newtag=None, newclosetag=None, useregex=False)` adds a new pair of tags, specified by `newtag` and `newclosetag`, around the pair of tags covering the specified position `pos` in string `s`. Returns `s` if there is no covering pair of tags.

!!! info
    If `newtag` is not specified, `tag` is used as the new open tag. Same for `newclosetag`. This only works properly when `useregex = False`.

``` python
# | denotes each specified position.
# == denotes each matched part.
# + denotes each added part.

#                 |
addtagpair("a$b$c$$d#ef#g", 6, r"\$|#", newtag='%', useregex=True)
#                ==
#          'a$b$c%$$%d#ef#g'
#                +==+

#               |
addtagpair("a(b(c()d)ef)g", 4, '(', ')')
#              ======
#          'a(b((c()d))ef)g'
#              +======+

#                 |
addtagpair("a<a>b<b>c<c></c>d</b>ef</a>g", 8, r"<\w+>", r"</\w+>", "<x>", "</x>", useregex=True)
#                ================
#          'a<a>b<x><b>c<c></c>d</b></x>ef</a>g'
#                +++================++++
```

### `changetagpair`

`changetagpair(s, pos, tag, closetag=None, newtag=None, newclosetag=None, useregex=False)` changes the pair of tags, specified by `newtag` and `newclosetag`, covering the specified position `pos` in string `s`. Returns `s` if there is no covering pair of tags.

!!! info
    If `newtag` is not specified, `tag` is used as the new open tag. Same for `newclosetag`. This only works properly when `useregex = False`.

``` python
# | denotes each specified position.
# == denotes each matched part.
# - denotes each removed part.
# + denotes each added part.

#                    |
changetagpair("a$b$c$$d#ef#g", 6, r"\$|#", newtag='%', useregex=True)
#                   --
#             'a$b$c%%d#ef#g'
#                   ++

#                  |
changetagpair("a(b(c()d)ef)g", 4, '(', ')', '[', ']')
#                 -====-
#             'a(b[c()d]ef)g'
#                 +====+

#                    |
changetagpair("a<a>b<b>c<c></c>d</b>ef</a>g", 8, r"<\w+>", r"</\w+>", "<x>", "</x>", useregex=True)
#                   ---=========----
#             'a<a>b<x>c<c></c>d</x>ef</a>g'
#                   +++=========++++
```

### `removetagpair`

`removetagpair(s, pos, tag, closetag=None, useregex=False, removecontent=False)` removes the pair of tags covering the specified position `pos` in string `s`. Returns `s` if there is no covering pair of tags.

- Option `removecontent` controls whether to remove the respective content as well.

``` python
# | denotes each specified position.
# == denotes each matched part.
# - denotes each removed part.

#                    |
removetagpair("a$b$c$$d#ef#g", 6, r"\$|#", useregex=True)
#                   --
#             'a$b$cd#ef#g'

#                    |
removetagpair("a$b$c$$d#ef#g", 6, r"\$|#", useregex=True, removecontent=True)
#                   --
#             'a$b$cd#ef#g'

#                  |
removetagpair("a(b(c()d)ef)g", 4, '(', ')')
#                 -====-
#             'a(bc()def)g'
#                 ====

#                  |
removetagpair("a(b(c()d)ef)g", 4, '(', ')', removecontent=True)
#                 ------
#             'a(bef)g'

#                    |
removetagpair("a<a>b<b>c<c></c>d</b>ef</a>g", 8, r"<\w+>", r"</\w+>", useregex=True)
#                   ---=========----
#             'a<a>bc<c></c>def</a>g'
#                   =========

#                    |
removetagpair("a<a>b<b>c<c></c>d</b>ef</a>g", 8, r"<\w+>", r"</\w+>", useregex=True, removecontent=True)
#                   ----------------
#             'a<a>bef</a>g'
```
