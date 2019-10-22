def FuzzNN(budget, n_rounds):
  """The main fuzzing framework.
  Args:
    budget: Sampling budget for seed selection
    n_rounds: Termination criteria for the fuzzer
  """
  inputs = init_inputs()
  for round in range(n_rounds):
    # ----- Input Selection -----
    "Select inputs with importance sampling"
    input_samples = sample_inputs(inputs, budget)
    "Compute the true edge coverage of the inputs"
    edge_true = get_coverage(input_samples)
    # ----- Mutation Location Selection -----
    "Initialize a fully connected Neural Network"
    NN = Neural_Network(X=input_samples, y=edge_true)
    "Train neural network with adaptive loss"
    NN = NN.train(loss=adaptive_loss)    
    "Compute gradients of edge coverage wrt. inputs"
    grad_vector = NN.compute_gradients()
    # ----- Mutation Operation -----
    "Mutate inputs to generate new inputs"
    new_inputs = mutate(input_samples, grad_vector)
    "Add new inputs to the pool of available inputs"
    inputs += new_inputs