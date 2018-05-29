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
[`jsontools`](functions/jsontools)     | 1           | Tools for operating JSON data.
[`mathtools`](functions/mathtools)     | 2           | Tools for math.
[`misctools`](functions/misctools)     | 2           | Tools for miscellaneous purposes.
[`printtools`](functions/printtools)   | 5           | Tools for printing purposes.
[`rangetools`](functions/rangetools)   | 8           | Tools for operating ranges/intervals.
[`recttools`](functions/recttools)     | 11          | Tools for operating rectangles.
[`seqtools`](functions/seqtools)       | 32          | Tools for operating sequences.
[`settools`](functions/settools)       | 10          | Tools for operating sets.
[`sortedtools`](functions/sortedtools) | 8           | Tools for operating sorted sequences.
[`stattools`](functions/stattools)     | 7           | Tools for statistics.
[`strtools`](functions/strtools)       | 12          | Tools for operating strings.
[`tabletools`](functions/tabletools)   | 14          | Tools for operating tables/matrices.

### By Tag

!!! info
    Only functions sharing similar logics are listed here.

Tag                   | Description                                         | Functions
----                  | ----                                                | ----
`cmp`                 | Compare objects/points/sequences.                   | [`misctools.cmp`](functions/misctools#cmp) - [`recttools.pointcmp`](functions/recttools#pointcmp) - [`seqtools.productcmp`](functions/seqtools#productcmp)
`flatten`             | Flatten nested dictionary/JSON object.              | [`dicttools.flatten`](functions/dicttools#flatten) - [`jsontools.flatten`](functions/jsontools#flatten)
`intersect`           | Compute the intersection between ranges/rectangles. | [`rangetools.intersect`](functions/rangetools#intersect) - [`recttools.intersect`](functions/recttools#intersect)
`union`               | Compute the union between ranges/rectangles.        | [`rangetools.union`](functions/rangetools#union) - [`recttools.union`](functions/recttools#union)
`issub*`              | Verify whether a sub-range/rectange/sequence.       | [`rangetools.issubrange`](functions/rangetools#issubrange) - [`recttools.issubrect`](functions/recttools#issubrect) - [`recttools.issubrect`](functions/recttools#issubrect) - [`seqtools.issubseq`](functions/seqtools/seqwithoutgap#issubseq) - [`seqtools.issubseqwithgap`](functions/seqtools/seqwithgap#issubseqwithgap) - [`sortedtools.issubsorted`](functions/sortedtools#issubsorted)
`*cover`              | Find the best sub-ranges/sets that cover the whole. | [`rangetools.rangecover`](functions/rangetools#rangecover) - [`settools.setcover`](functions/settools#setcover)
`bestsub*`            | Find the best sub-set/sequence.                     | [`seqtools.bestsubseq`](functions/seqtools#bestsubseq) - [`seqtools.bestsubseqwithgap`](functions/seqtools#bestsubseqwithgap) - [`settools.bestsubset`](functions/settools#bestsubset)
`commonsub*`          | Find the common sub-sequence/substring.             | [`seqtools.commonsubseq`](functions/seqtools/seqwithoutgap#commonsubseq) - [`seqtools.commonsubseqwithgap`](functions/seqtools/seqwithgap#commonsubseqwithgap) - [`sortedtools.sortedcommon`](functions/sortedtools#sortedcommon) - [`strtools.commonsubstr`](functions/strtools#commonsubstr)
`match`               | Match common elements among sequences.              | [`seqtools.match`](functions/seqtools#match) - [`sortedtools.sortedmatch`](functions/sortedtools#sortedmatch)
`join`                | Join sequences/tables.                              | [`seqtools.join`](functions/seqtools#join) - [`seqtools.cmpjoin`](functions/seqtools#cmpjoin) - [`sortedtools.sortedjoin`](functions/sortedtools#sortedjoin) - [`tabletools.join`](functions/tabletools#join)
`matchingfrequencies` | Compute the frequency of each item among sequences. | [`seqtools.matchingfrequencies`](functions/seqtools#matchingfrequencies) - [`sortedtools.matchingfrequencies`](functions/sortedtools#matchingfrequencies)
`*2grams`             | Convert sequence/string to grams.                   | [`seqtools.seq2grams`](functions/seqtools#seq2grams) - [`strtools.str2grams`](functions/strtools#str2grams)

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
