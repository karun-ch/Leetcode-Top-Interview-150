class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""  # Handle empty input

        # Take the first string as the initial prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for string in strs:
            while not string.startswith(prefix):
                # Reduce the prefix by removing the last character
                prefix = prefix[:-1]
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""

        return prefix
