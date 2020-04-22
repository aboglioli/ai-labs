def is_final_state_jarras(state):
  if state[0] == 2:
    return True
  else:
    return False
  
  
  
print(is_final_state_jarras((1,1)))
print(is_final_state_jarras((2,7)))