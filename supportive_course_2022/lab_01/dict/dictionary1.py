a_dict = {
    "aggelos": 123,
    "dimitris": 234,
    "giannis": 412,
    "maria": 154,
    "xristos": 456,
    "vasilis": 789,
}

# iteration
for key in a_dict:
    print(f"όνομα {key} κωδικός {a_dict[key]}")

for key, value in a_dict.items():
    print(f"όνομα {key} κωδικός {value}")

