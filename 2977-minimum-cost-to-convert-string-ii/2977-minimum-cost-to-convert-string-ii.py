class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18
        n = len(source)

        mp = {}
        idx = 0
        for s in original:
            if s not in mp:
                mp[s] = idx
                idx += 1
        for s in changed:
            if s not in mp:
                mp[s] = idx
                idx += 1

        N = idx
        dist = [[INF]*N for _ in range(N)]
        for i in range(N):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = mp[o]
            v = mp[c]
            if w < dist[u][v]:
                dist[u][v] = w

        for k in range(N):
            dk = dist[k]
            for i in range(N):
                di = dist[i]
                ik = di[k]
                if ik == INF:
                    continue
                for j in range(N):
                    v = ik + dk[j]
                    if v < di[j]:
                        di[j] = v

        class Trie:
            __slots__ = ("nxt", "id")
            def __init__(self):
                self.nxt = {}
                self.id = -1

        def insert(root, s, i):
            node = root
            for ch in s:
                node = node.nxt.setdefault(ch, Trie())
            node.id = i

        srcTrie = Trie()
        tgtTrie = Trie()

        idToStr = [""] * N
        for s, i in mp.items():
            idToStr[i] = s

        for i in range(N):
            insert(srcTrie, idToStr[i], i)
            insert(tgtTrie, idToStr[i], i)

        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            sNode = srcTrie
            tNode = tgtTrie

            for j in range(i, n):
                sNode = sNode.nxt.get(source[j])
                tNode = tNode.nxt.get(target[j])
                if sNode is None or tNode is None:
                    break
                sid = sNode.id
                tid = tNode.id
                if sid != -1 and tid != -1:
                    c = dist[sid][tid]
                    if c < INF:
                        v = c + dp[j + 1]
                        if v < dp[i]:
                            dp[i] = v

        return -1 if dp[0] >= INF else dp[0]
