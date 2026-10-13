
class Solution:
    def replaceWords(self, dictionary, sentence):
        roots = set(dictionary)
        words = sentence.split()
        result = []

        for word in words:
            replaced = word

            for i in range(1, len(word) + 1):
                prefix = word[:i]

                if prefix in roots:
                    replaced = prefix
                    break

            result.append(replaced)

        return " ".join(result)
