mytuple = ("nikos", 21, "pappas", 21, True)
for x in mytuple:
    print(x)

print("Count 21:", mytuple.count(21))
print("Count nikos:", mytuple.count("nikos"))
print("Count False:", mytuple.count(False))