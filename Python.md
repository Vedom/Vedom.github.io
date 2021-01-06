[Home](index.md)
# Python
#### Necessary functions? Not necessarily. But here they are anyway.

These two are inspired by this blog [here](https://towardsdatascience.com/there-is-no-argmax-function-for-python-list-cd0659b05e49).

```python
def get_list_argmax(l):
  """Finds the index of a list's maximum value.

  Args:
    l: list, default: None, List of numbers.
  Returns:
    argmax: int, The index of the maximum value in the list.
  """
  return max(zip(l, range(len(l))))[1]
```


```python
def get_list_argmin(l):
  """Finds the index of a list's minimum value.

  Args:
    l: list, default: None, List of numbers.
  Returns
    argmax: int, The index of the maximum value in the list.
  """
  return min(zip(l, range(len(l))))[1]
```

```python
def get_all_weekday_dates_in_year(yr, wkday):
  """Returns all dates from a year for a given weekday.

  Args:
    yr: Year during which dates are needed.
    wkday: Weekday for which dates are needed. Can enter
      only first two letters of weekday.
  Returns:
    A list of dates in string format YYYY-MM-DD
  """
  from datetime import date, timedelta
  weekdays = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su'] # 0==Monday
  wkday = wkday.lower()[:2]
  dow_num = next(idx for idx,obj in enumerate(weekdays) if obj==wkday)
  first_7_days_of_year = [(date(yr, 1, 1) + timedelta(days=x)).weekday() for x in range(7)]
  next_dow = next(idx for idx,obj in enumerate(first_7_days_of_year) if obj==dow_num)
  d = date(yr, 1, 1)  # January 1st
  d += timedelta(days = next_dow)  # First wkday in yr
  dow_dates_in_year = []
  while d.year == yr:
    dow_dates_in_year.append(d.strftime("%Y-%m-%d"))
    d += timedelta(days = 7)
  return dow_dates_in_year
```
