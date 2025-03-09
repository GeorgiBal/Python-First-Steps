def permute(string, pocket=''):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)

print(permute('ABC'))