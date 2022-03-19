if __name__ == "__main__":
    a_dict = {
        "aggelos": 123,
        "dimitris": 234,
        "giannis": 412,
        "maria": 154,
        "xristos": 456,
        "vasilis": 789,
    }

    # add
    a_dict["kostas"] = 999
    # modify
    a_dict["aggelos"] = 321
    # del
    del a_dict["dimitris"]

    for key, value in a_dict.items():
        print(f"όνομα {key} κωδικός {value}")
