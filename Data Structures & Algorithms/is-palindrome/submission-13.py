class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: left (i) at start, right (j) at end
        i = 0
        j = len(s) - 1

        while i < j:
            # Skip non-alphanumeric characters from the left
            if not s[i].isalnum():
                i += 1
                continue  # go back to check while condition and skip comparison

            # Skip non-alphanumeric characters from the right
            if not s[j].isalnum():
                j -= 1
                continue

            # Now both s[i] and s[j] are alphanumeric → compare them (case‑insensitive)
            if s[i].lower() == s[j].lower():
                # Characters match → move both pointers inward
                i += 1
                j -= 1
            else:
                # Mismatch found → not a palindrome
                return False

        # All pairs matched → it's a palindrome
        return True