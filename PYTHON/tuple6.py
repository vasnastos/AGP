mytuple = ("nikos", 21, "pappas", 21, True)
for x in mytuple:
    print(x)


print('mytuple.index("nikos"): ', mytuple.index("nikos"))
print("mytuple.index(21): ", mytuple.index(21))
print("mytuple.index(21, 2): ", mytuple.index(21, 2))
print(
    "mytuple.index(21, mytuple.index(21)+1): ", mytuple.index(21, mytuple.index(21) + 1)
)
