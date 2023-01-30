# Credits: Jordan Chong, The Phoenixes

vowels = 'aeiou'
consonants = 'mnptkswjl'
illegal = ['wu', 'wo', 'ji', 'ti', 'nn', 'nm']

def solve(W: str) -> str:
    answer = 'pona'

    for y in range(len(W)):
        x = W[y]

        if W[y:y+2] in illegal:
            answer = 'ike'
            break

        if x not in vowels and x not in consonants:
            answer = 'ike'
            break

        if len(W[y:y+2]) == 2 and W[y] in vowels and W[y+1] in vowels:
            answer = 'ike'
            break
    
    p = 0
    while p < len(W):
        if is_valid_syllable(W[p:p+3]):
            p += 3
        elif is_valid_syllable(W[p:p+2]):
            p += 2
        elif is_valid_syllable(W[p:p+1]):
            p += 1
        else:
            answer = 'ike'
            break
    
    return answer

def is_valid_syllable(s):
    if len(s) == 1:
        return s in vowels
    elif len(s) == 2:
        return s[0] in consonants and s[1] in vowels or s[0] in vowels and s[1] == 'n'
    elif len(s) == 3:
        return s[0] in consonants and s[1] in vowels and s[2] == 'n'
    else:
        return False

def main():
    T = int(input())
    for _ in range(T):
        W = input()
        print(solve(W))

if __name__ == '__main__':
    main()
