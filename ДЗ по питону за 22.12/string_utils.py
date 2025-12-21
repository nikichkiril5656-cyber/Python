def polyndrom(text):
    return text[::-1] == text
def anagram(s1, s2):
    s1_clean = ''.join(c.lower() for c in s1 if c.isalnum())
    s2_clean = ''.join(c.lower() for c in s2 if c.isalnum())
    return sorted(s1_clean) == sorted(s2_clean)
def reverse_text(text):
    return text[::-1]