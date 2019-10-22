def sample_inputs(all_inputs, max_budget):
  """Importance sampling based input selection.
  Returns:
    A sample of the most important input.
  """
  budget = max_budget
  selected_inputs = []
  edges = get_coverage(all_inputs)
  "Sort the inputs from most to least recent" 
  sorted_inputs = sort_by_recency(all_inputs)
  "Sort the new edges from most to least rare"
  important_edges = sort_by_rarity(new_edges) 
  for edge in important_edges:
    for input in sorted_inputs:
        if budget == 0:
             break
        if edge_cov[input][edge] == 1:
            selected_inputs.append(input)
            budget = budget - 1
  return selected_inputs




