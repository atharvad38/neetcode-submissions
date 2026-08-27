class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g_map = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key in g_map:
                g_map[key].append(s)
            else:
                g_map[key] = [s]

        return list(g_map.values())