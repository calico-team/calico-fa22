# Credits: Jordan Chong, The Phoenixes

vowels = 'aeiou'
consonants = ['m', 'n', 'p', 't', 'k', 's', 'w', 'j', 'l']
illegal = ['wu', 'wo', 'ji', 'ti', 'nn', 'nm']

def solve(W: str) -> str:
    first_syllable = ''
    answer = 'pona'

    for y in range(len(W)):
        x = W[y]
        z = W[y:y+2]
        if z in illegal:
            answer = 'ike'
            break
        if x not in vowels and x not in consonants:
            answer = 'ike'
            break
        if len(z) == 2 and z[0] in vowels and z[1] in vowels:
            answer = 'ike'
            break
    
    p = 0
    
    for y in range(len(W)):
        current_letter = W[y]

        if len(first_syllable) == 0:
            first_syllable += current_letter
        elif len(first_syllable) == 1:
            if first_syllable[0] in consonants:
                if current_letter not in vowels:
                    answer = 'ike'
                    break
                else:
                    first_syllable += current_letter
            elif first_syllable[0] in vowels:
                if current_letter == 'n':
                    p = 2
                    break
                elif current_letter in consonants:
                    p = 1
                    break
        elif len(first_syllable) == 2:
            if current_letter == 'n':
                p = 3
                break
            elif current_letter in consonants:
                p = 2
                break
    
    if p == len(W):
        return answer
    else:
        second_syllable = W[p:]
        if second_syllable[0] in vowels:
            if len(second_syllable) != 1:
                if second_syllable[1] != 'n' and second_syllable[1] in consonants:
                    answer = 'ike'
        elif second_syllable[0] in consonants:
            # no vowel, so ike
            if len(second_syllable) == 1:
                answer = 'ike'
            elif second_syllable[1] in consonants:
                answer = 'ike'
            elif second_syllable[1] in vowels:
                if len(second_syllable) == 3:
                    if second_syllable[2] != 'n' and second_syllable[1] in consonants:
                        answer = 'ike'
        return answer
def main():
    T = int(input())
    for _ in range(T):
        W = input()
        print(solve(W))

if __name__ == '__main__':
    main()
