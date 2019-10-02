def h_bellwether(cluster_tree):
  bellwethers = {}
  def bellwether(list1, list2):
    for source in list1:
    clf = LR(source)
    _list2 = list2.pop(source)
    for dest in _list2:
      score[source][dest] = clf.predict(dest)
    return best(score.key())

  for level in cluster_tree.levels:
    if level == cluster_tree.max_level:
      for c in cluster_tree[level].clusters:
        bellwethers[c] = bellwether(c.proj)
    else:
      for c in cluster_tree[level].clusters:
        _bell = bellwethers[c.child]
        bellwethers[c] = bellwether(_bell)
  return bellwethers
