def hamming_distance(s1,s2):
    return len([True for i in range(len(s1)) if s1[i]!=s2[i]]) if len(s1)==len(s2) else -1


if __name__ == '__main__':
    a="ABCGHG"
    b="BCCGHC"
    print(hamming_distance(a,b))