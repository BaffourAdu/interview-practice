
# WHO'S THE HEAD OF STATE?
# According to the Ghanaian constitution, the order of persons that can be Head of 
# State are President, Vice President, Speaker of Parliament, Chief Justice, in 
# \decreasing order of preference order. That is, the Vice President can become 
# Head of State if and only if the President is unable to perform their duties. 
# Likewise the Chief Justice can become the Head of State if and only if the 
# President, Vice President, and Speaker of Parliament are incapacitated. 

# Given a list of these roles, you're required to judge who in the list is the most 
# qualified Head of State. All possible roles are:

# - President
# - Vice President
# - Speaker of Parliament
# - Chief Justice
# - MCE (can appear multiple times)
# - Mayor (can appear multiple times)
# - Member of Parliament (can appear multiple times)
# - Citizen (can appear multiple times)

# CONSTRAINTS:
# - You can loop through the list just once, and with the pop and length operations. 
# (All other array/list operations are prohibited)
# - You cannot rebuild the list

# Example input and expected output:
# [Vice President, Chief Justice, Speaker of Parliament] => Vice President
# [Chief Justice, Speaker of Parliament, Vice President, President] => President
# [Speaker of Parliament, Member of Parliament, MCE] => Speaker of Parliament
# [MCE, Mayor, Chief Justice] => Chief Justice
# [Member of Parliament, MCE, Mayor] => None



def mostQualifiedHead(head_of_states):

  head_of_states_ranking = {
    'President': 8,
    'Vice President': 7,
    'Speaker of Parliament': 6,
    'Chief Justice': 5,
    'MCE': 4,
    'Mayor': 3,
    'Member of Parliament': 2,
    'Citizen': 1
  }

  maximum_rank = 0
  maximum_head_of_state = None

  for head_of_state in head_of_states:
    if head_of_states_ranking[head_of_state] > maximum_rank:
      maximum_rank = head_of_states_ranking[head_of_state]
      maximum_head_of_state = head_of_state

  print(maximum_head_of_state)


test_case1 = ["MCE", "Mayor", "Chief Justice"]
test_case2 = ["Vice President", "Chief Justice", "Speaker of Parliament"]
test_case3 = ["Member of Parliament", "MCE", "Mayor"]

mostQualifiedHead(test_case2)