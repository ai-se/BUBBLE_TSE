def CFS(data):
  features = []
  score = -1e-9
  while True:
    best_feature = None
    for feature in range(data.features):
      features.append(feature)
      temp_score = calculate_corr(data[F])
      if temp_score > score:
        score = temp_score
        best_feature = features
      features.pop()
    features.append(best_feature)
    if not improve(score):
      break
  return features
