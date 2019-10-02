def BUBBLE(data):
  project_features = get_features(data)
  cluster_tree = BIRCH(project_features)
  bellwethers = h_bellwether(cluster_tree)
  for project in test_1:
    train_2, test_2 = tt_split(data[project])
    self_clf = LR(train_2)
    b_clf = find_bellw(project_features[project])
    self_score = self_clf.predict(test_2)
    bellwether_score = b_clf.predict(test_2)
    results += [self_score, bellwether_score]
  return results
