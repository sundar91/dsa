def solve(A):
    c = 0
    countVowel = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(0, len(A)):
        if A[i] in vowels :
            countVowel += 1
        if countVowel >= 1:               
            c = c + countVowel
    return c  % 10003

print(solve("pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn"))