from collections import Counter
if __name__=='__main__':
    zen_of_python="""
    The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

    """

    all_together=Counter(zen_of_python)
    chars={chr(x):all_together[chr(x)]+all_together[chr(x).lower()] for x in range(65,91)}
    print(chars)

    #Alternative
    chars={chr(x):0 for x in range(65,91)}
    for chr_x in list(zen_of_python):
        if chr_x.upper() in chars:
            chars[chr_x.upper()]+=1
    print(chars)