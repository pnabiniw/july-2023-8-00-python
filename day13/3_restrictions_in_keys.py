# 1. The dictionary value can be of any datatype
# 2. But, the dictionary key must be an immutable datatype

data = {"name": "Jon", 2: 12, (1, 2): "Ram", 2.2: ["Hary", "Ram", "Jon"]}  # Valid dictionary
# invalid_d = {[1, 2]: "Sita", {1 , 2}: 12, ([1, 2], 3): "Ram"}  # Invalid dictionry
