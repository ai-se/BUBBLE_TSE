def mutate(sampled_inputs, gradients):
    "Mutate inputs with gradient ascent"
    mutated_inputs = []
    for old_input in sampled_inputs:
      for i in old_input:
        new_input[i] = old_input[byte] + step * gradients[i]
      mutated_inputs.append(new_input)
    return mutated_inputs