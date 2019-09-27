# PySpark

``` pyspark
check_uniqueness(dat1, dat2, id_col)
  """Checks whether two dataframes have any overlapping
  unique identifiers.

  Parameters
  ----------
  dat1: spark dataframe, default: None
    First spark dataframe to check.
  dat2: spark dataframe, default: None
    Second spark dataframe to check.
  id_col: col, default: None
    Unique identifier column.

  Returns
  -------
  overlap_count: int
    Count of identifiers in both dataframes.
    0 if no overlap between dataframes' identifiers.
  dat1_repeat_count: int
    Count of redundant rows of identifiers for dat1.
    0 if all rows distinct.
  dat2_repeat_count: int
    Count of redundant rows of identifiers for dat2.
    0 if all rows distinct.
  """
  overlap_count = dat1.join(dat2, [id_col]).count()
  dat1_repeat_count = dat1.select(id_col).count() - dat1.select(id_col).distinct().count()
  dat2_repeat_count = dat2.select(id_col).count() - dat2.select(id_col).distinct().count()
  return overlap_count, dat1_repeat_count, dat2_repeat_count
```
