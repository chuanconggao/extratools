!!! info
    For introduction of this library, please refer to [README](README).

## Functions

### By Tools

!!! info
    All the functions are organized as follows.

Tools                                  | # Functions | Description
----                                   | ----       :| ----
[`debugtools`](functions/debugtools)   | 4           | Tools for debugging purposes.
[`dicttools`](functions/dicttools)     | 7           | Tools for operating dictionaries.
[`gittools`](functions/gittools)       | 1           | Tools for interacting with Git.
[`graphtools`](functions/graphtools)   | 1           | Tools for graph.
[`htmltools`](functions/htmltools)     | 1           | Tools for operating HTML data.
[`jsontools`](functions/jsontools)     | 1           | Tools for operating JSON data.
[`mathtools`](functions/mathtools)     | 2           | Tools for math.
[`misctools`](functions/misctools)     | 2           | Tools for miscellaneous purposes.
[`printtools`](functions/printtools)   | 5           | Tools for printing purposes.
[`rangetools`](functions/rangetools)   | 8           | Tools for operating ranges/intervals.
[`recttools`](functions/recttools)     | 11          | Tools for operating rectangles.
[`seqtools`](functions/seqtools)       | 34          | Tools for operating sequences.
[`settools`](functions/settools)       | 11          | Tools for operating sets.
[`sortedtools`](functions/sortedtools) | 9           | Tools for operating sorted sequences.
[`stattools`](functions/stattools)     | 7           | Tools for statistics.
[`strtools`](functions/strtools)       | 15          | Tools for operating strings.
[`tabletools`](functions/tabletools)   | 16          | Tools for operating tables/matrices.

### By Tag

!!! info
    Only functions sharing similar logics among different categories are listed here.

Tag                   | Description                                                          | Functions
----                  | ----                                                                 | ----
`cmp`                 | Compare objects/points/sequences.                                    | [`misctools.cmp`](functions/misctools#cmp) <br/> [`recttools.pointcmp`](functions/recttools#pointcmp) <br/> [`seqtools.productcmp`](functions/seqtools#productcmp)
`flatten`             | Flatten nested dictionary/JSON object.                               | [`dicttools.flatten`](functions/dicttools#flatten) <br/> [`jsontools.flatten`](functions/jsontools#flatten)
`intersect`           | Compute the intersection between ranges/rectangles/sorted sequences. | [`rangetools.intersect`](functions/rangetools#intersect) <br/> [`recttools.intersect`](functions/recttools#intersect) <br/> [`sortedtools.sortedcommon`](functions/sortedtools#sortedcommon)
`union`               | Compute the union between ranges/rectangles/sorted sequences.        | [`rangetools.union`](functions/rangetools#union) <br/> [`recttools.union`](functions/recttools#union) <br/> [`sortedtools.sortedall`](functions/sortedtools#sortedall)
`issub*`              | Verify whether a sub-range/rectangle/sequence.                       | [`rangetools.issubrange`](functions/rangetools#issubrange) <br/> [`recttools.issubrect`](functions/recttools#issubrect) <br/> [`seqtools.issubseq`](functions/seqtools/seqwithoutgap#issubseq) <br/> [`seqtools.issubseqwithgap`](functions/seqtools/seqwithgap#issubseqwithgap) <br/> [`sortedtools.issubsorted`](functions/sortedtools#issubsorted)
`*cover`              | Find the best sub-ranges/sets that cover the whole.                  | [`rangetools.rangecover`](functions/rangetools#rangecover) <br/> [`settools.setcover`](functions/settools#setcover)
`bestsub*`            | Find the best sub-set/sequence.                                      | [`seqtools.bestsubseq`](functions/seqtools#bestsubseq) <br/> [`seqtools.bestsubseqwithgap`](functions/seqtools#bestsubseqwithgap) <br/> [`settools.bestsubset`](functions/settools#bestsubset)
`commonsub*`          | Find the common sub-sequence/substring.                              | [`seqtools.commonsubseq`](functions/seqtools/seqwithoutgap#commonsubseq) <br/> [`seqtools.commonsubseqwithgap`](functions/seqtools/seqwithgap#commonsubseqwithgap) <br/> [`sortedtools.sortedcommon`](functions/sortedtools#sortedcommon) <br/> [`strtools.commonsubstr`](functions/strtools#commonsubstr)
`euumeratesub*`       | Enumerate all the sub-sequences/sets.                                | [`seqtools.enumeratesubseqs`](functions/seqtools/seqwithoutgap#enumeratesubseqs) <br/> [`seqtools.enumeratesubseqswithgap`](functions/seqtools/seqwithgap#enumeratesubseqswithgap) <br/> [`settools.enumeratesubsets`](functions/settools#enumeratesubsets) <br/> [`strtools.enumeratesubstrs`](functions/strtools#enumeratesubstrs)
`match`               | Match common elements among sequences.                               | [`seqtools.match`](functions/seqtools#match) <br/> [`sortedtools.sortedmatch`](functions/sortedtools#sortedmatch)
`join`                | Join sequences/tables.                                               | [`seqtools.join`](functions/seqtools#join) <br/> [`seqtools.cmpjoin`](functions/seqtools#cmpjoin) <br/> [`sortedtools.sortedjoin`](functions/sortedtools#sortedjoin) <br/> [`tabletools.join`](functions/tabletools#join)
`matchingfrequencies` | Compute the frequency of each item among sequences.                  | [`seqtools.matchingfrequencies`](functions/seqtools#matchingfrequencies) <br/> [`sortedtools.matchingfrequencies`](functions/sortedtools#matchingfrequencies)
`merge*`              | Merge sequence/table without conflict.                               | [`seqtools.mergeseqs`](functions/seqtools#mergeseqs) <br/> [`tabletools.mergecols`](functions/tabletools#mergecols)
`sorted*`             | Sort sequence/table.                                                 | [`seqtools.sortedbyrank`](functions/seqtools#sortedbyrank) <br/> [`seqtools.sortedtorank`](functions/seqtools#sortedtorank) <br/> [`tabletools.sortedbycol`](functions/tabletools#sortedbycol)
`filterby*`           | Filter sequence/table.                                               | [`seqtools.filterbyother`](functions/seqtools#filterbyother) <br/> [`tabletools.filterbycol`](functions/tabletools#filterbycol)
`*2grams`             | Convert sequence/string to grams.                                    | [`seqtools.seq2grams`](functions/seqtools#seq2grams) <br/> [`strtools.str2grams`](functions/strtools#str2grams)

## Data Structures

Class                                                      | Description
----                                                       | ----
[`defaultlist.DefaultList`](datastructures/defaultlist)    | A sub-class of `list` that grows if necessary when accessing.
[`disjointsets.DisjointSets`](datastructures/disjointsets) | Disjoint sets.
[`segmenttree.SegmentTree`](datastructures/segmenttree)    | Segment tree.

## CLI Tools

Name                                              | Description
----                                              | ----
[`extratools-remap`](cli#dicttools.remap)         | CLI for [`dicttools.remap`](functions/dicttools#remap).
[`extratools-flatten`](cli#jsontools.flatten)     | CLI for [`jsontools.flatten`](functions/jsontools#flatten).
[`extratools-teststats`](cli#stattools.teststats) | CLI for [`stattools.teststats`](functions/stattools#teststats).
