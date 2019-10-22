def adaptive_loss(egde_true, edge_pred):
    "Coverage guided loss function to train Neural Network."
    penalty = get_neg_pos_ratio()
    loss = 0
    for true, pred, b in zip(edge_true, edge_pred, penalty):
      loss += -(b*true*log(pred) + (1-true)*log((1-pred)))
    return loss