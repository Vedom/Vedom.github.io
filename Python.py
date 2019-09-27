def get_list_argmax(l):
  """Finds the index of a list's maximum value.

  Parameters
  ----------
  l: list, default: None
    List of numbers.

  Returns
  -------
  argmax: int
    The index of the maximum value in the list.
  """
  return max(zip(l, range(len(l))))[1]

def get_list_argmin(l):
  """Finds the index of a list's minimum value.

  Parameters
  ----------
  l: list, default: None
    List of numbers.

  Returns
  -------
  argmax: int
    The index of the maximum value in the list.
  """
  return min(zip(l, range(len(l))))[1]
