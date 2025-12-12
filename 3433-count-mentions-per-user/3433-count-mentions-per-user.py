class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        from collections import defaultdict

        groups = defaultdict(list)
        ts = []
        for e in events:
            t = int(e[1])
            if t not in groups:
                ts.append(t)
            groups[t].append(e)
        ts.sort()

        mentions = [0]*numberOfUsers
        online = [True]*numberOfUsers
        recover = [-1]*numberOfUsers

        for t in ts:
            for i in range(numberOfUsers):
                if recover[i] != -1 and recover[i] <= t:
                    online[i] = True
                    recover[i] = -1

            for e in groups[t]:
                if e[0] == "OFFLINE":
                    u = int(e[2])
                    online[u] = False
                    recover[u] = t + 60

            for e in groups[t]:
                if e[0] == "MESSAGE":
                    s = e[2]
                    if s == "ALL":
                        for i in range(numberOfUsers):
                            mentions[i] += 1
                    elif s == "HERE":
                        for i in range(numberOfUsers):
                            if online[i]:
                                mentions[i] += 1
                    else:
                        for tok in s.split():
                            if tok.startswith("id"):
                                mentions[int(tok[2:])] += 1

        return mentions

