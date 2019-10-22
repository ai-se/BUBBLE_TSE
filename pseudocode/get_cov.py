def get_coverage(inputs):
  """Get edge coverage.
  Returns:
    A dictionary of inputs and corresponding coverage
  """
  cov_dict = dict()
  for test_input in inputs:
    "Get coverage by running the program"
    cov = coverage(input)
    "Update coverage dictionary of test input"
    cov_dict[test_input] = cov
  return cov_dict