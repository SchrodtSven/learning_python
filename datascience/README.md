# Resources 

 - https://dataorigami.net/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/
 - https://pandas.pydata.org/docs/user_guide/cookbook.html
 - https://code.datasciencedojo.com/datasciencedojo/datasets


 - https://public.opendatasoft.com/explore/dataset/geonames-all-cities-with-a-population-1000/table/?disjunctive.cou_name_en&sort=name&refine.cou_name_en=France 
 - https://stackoverflow.com/questions/45759891/correct-use-of-map-for-mapping-a-function-onto-a-df-python-pandas
 
- https://www.kaggle.com/datasets/sazidthe1/data-science-salaries [reg. needed]

# vis
 - scatterplot

# Keep in mind:

- The Python and NumPy <i>indexing operators</i> <code>[]</code> and <i>attribute operator</i> <code>.</code> provide quick and easy access to pandas data structures across a wide range of use cases. This makes interactive work intuitive, as there’s little new to learn if you already know how to deal with it

<code>.loc</code> is primarily label based, but may also be used with a boolean array. <code>.loc</code>  will raise <code>KeyError</code> when the items are not found. Allowed inputs are:

        A single label, e.g. 5 or 'a' (Note that 5 is interpreted as a label of the index. This use is not an integer position along the index.).

        A list or array of labels ['a', 'b', 'c'].

        A slice object with labels 'a':'f' (Note that contrary to usual Python slices, both the start and the stop are included, when present in the index! See Slicing with labels and Endpoints are inclusive.)

        A boolean array (any NA values will be treated as False).

        A callable function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above).

        A tuple of row (and column) indices whose elements are one of the above inputs.

