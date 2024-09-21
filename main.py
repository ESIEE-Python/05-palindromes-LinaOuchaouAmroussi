"""
Cette fonction teste si il s'agit d'un palindrome ou pas"""
def ispalindrome(s):
    """Cette fonction este si s est un palindrome
    :param s: la chaine de caractères
    :return "s est un palindrome et false sinon
    """
    accents = "àéèùîïçêâôöëûüÂÊÎÔÛÄËÏÖÜÀÇÉÈÙ"
    sans_accents = "aeeuiiceaooeuuAEIOUAEIOUACEEU"
    trantab = str.maketrans(accents, sans_accents)
    s = s.translate(trantab)
    ponctuation = ".,!?;:«»'\"-()[]{}"
    trantab_punct = str.maketrans('', '', ponctuation)
    s = s.translate(trantab_punct)
    s = s.replace(" ", "")
    s = s.lower()
    return s  == s[::-1]
def main():
    """ 
    Fonction principale pour tester si ce sont des palindromes ou pas"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
