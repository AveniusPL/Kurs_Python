def isPalindrome(s):
    lewy_indeks = 0
    prawy_indeks = len(s) - 1
    while lewy_indeks < prawy_indeks:
        if not s[lewy_indeks] == s[prawy_indeks]:
            return False
        lewy_indeks += 1
        prawy_indeks -= 1
    return True
print(isPalindrome('aza'))
print(isPalindrome('kajak'))
print(isPalindrome('niekajak'))