[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/gittools.py)

!!! danger
    [Git](https://git-scm.com/) must be properly installed and accessible on `PATH`.

## Parsing Output

Tools for parsing the output of Git.

### `status`

`status(path='.')` returns the status of Git at the directory `path` in JSON object, in default to the current directory. Returns `None` if not a Git repository.

!!! warning
    If a submodule has untracked files, Git reports the whole submodule as modified.

``` python
# Not a Git repository.
status('~')
# None

status()
# {'path'   : '.',
#  'oid'    : '932451b735ee3969efb52f4964358b57af6a730e',
#  'branch' : {'head': 'master', 'upstream': 'origin/master'},
#  'commits': {'ahead': 0, 'behind': 0},
#  'files'  : {'modified' : ['README.md',
#                            'docs/index.md',
#                            'setup.py'],
#              'untracked': ['docs/functions/gittools.md',
#                            'extratools/gittools.py']}}

# The submodules have untracked files, thus labelled as modified.
status("~/Dot Files")
# {'path'   : '~/Dot Files',
#  'oid'    : '053a20463e3f33eaae955a68d2f287180d7c310a',
#  'branch' : {'head': 'master', 'upstream': 'origin/master'},
#  'commits': {'ahead': 0, 'behind': 0},
#  'files'  : {'modified' : ['.vim/bundle/YouCompleteMe',
#                            '.vim/bundle/vim-LanguageTool',
#                            '.vim/bundle/vim-dispatch'],
#              'untracked': []}}

status("~/Dot Files/.vim/bundle/YouCompleteMe")
# {'path'   : '~/Dot Files/.vim/bundle/YouCompleteMe',
#  'oid'    : '2dcb3e91adf6b6df452abd7e644649c376759427',
#  'branch' : {'head': None, 'upstream': None},
#  'commits': {'ahead': 0, 'behind': 0},
#  'files'  : {'modified' : [],
#              'untracked': ['third_party/ycmd']}}
```
