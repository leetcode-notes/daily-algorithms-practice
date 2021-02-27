class Solution:
    def entityParser(self, text: str) -> str:
        html_entities = {"&quot;": "\"", "&apos;": "'",
                         "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        for k, v in html_entities.items():
            text = text.replace(k, v)
        text = text.replace("&amp;", "&")
        return text


"""
Success
Details 
Runtime: 40 ms, faster than 98.88% of Python3 online submissions for HTML Entity Parser.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for HTML Entity Parser.
Next challenges:
Group Shifted Strings
Exclusive Time of Functions
Get Watched Videos by Your Friends
"""
