# merge


def merge(D1, D2, priority):
  higher = D1
  lower = D2
  if priority == "second":
    lower = D1
    higher = D2
  D3 = {}
  for key in lower:
    D3[key] = lower[key]
  for key in higher:
    D3[key] = higher[key]
  return D3

