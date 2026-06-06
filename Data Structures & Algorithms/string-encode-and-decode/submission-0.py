class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_string = ""
        for i in strs:
            encoded_string = encoded_string + i + "é"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        m = ""
        for i in s:
            if i != "é":
                m+=i
            elif i == "é":
                decoded_strs.append(m)
                m = ""
        return decoded_strs