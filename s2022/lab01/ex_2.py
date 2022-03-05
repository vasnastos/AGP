if __name__=='__main__':
    str_in="How I need a drink alcoholic of course, after all those lectures involving quantum mechanics"
    for word in str_in.split():
        print(f'{word}-{len(word)}')