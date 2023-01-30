# Credits: Jordan Chong, The Phoenixes

vowels = 'aeiou'
consonants = 'mnptkswjl'
illegal = ['wu', 'wo', 'ji', 'ti', 'nn', 'nm']

def solve(W: str) -> str:
    answer = 'pona'

    # starts with 'n' edge case
    if W[0] == 'n':
        if len(W) > 1:
            if W[1] not in vowels:
                answer = 'ike'
        else:
            answer = 'ike'
    
    for x in range(len(W)):
        # checks for illegal letters
        if W[x] not in vowels and W[x] not in consonants:
            answer = 'ike'
        
        # W[x] + W[x+1] (if it exists)
        a = W[x:x + 2]
        if len(a) == 1:
            # ends in non-n consonant edge case
            if a[0] in consonants and a[0] != 'n':
                answer = 'ike'
        # illegal sequences
        elif a in illegal:
            answer = 'ike'
            break
        # adjacent vowels
        elif a[0] in vowels and a[1] in vowels:
            answer = 'ike'
            break
        # adjacent consonants (where first is not n)
        elif a[0] in consonants and a[0] != 'n' and a[1] in consonants:
            answer = 'ike'
            break

    return answer

def main():
    T = int(input())
    for _ in range(T):
        W = input()
        print(solve(W))

if __name__ == '__main__':
    main()
