# stack

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        pre_time = 0
        pre_task = None
        res = dict([(i, 0) for i in range(n)])
        for log in logs:
            function, state, time = log.split(':')
            function = int(function)
            time = int(time)
            if state == 'start':
                stack.append(function)
                if pre_task is not None:
                    res[pre_task] += time-pre_time
                pre_task = stack[-1]
            elif state == 'end':
                time += 1
                stack.pop()
                res[function] += time-pre_time
                if stack:
                    pre_task = stack[-1]
                else:
                    pre_task = None
            pre_time = time
        res = sorted([item for item in res.items()], key=lambda x:x[0])
        res = [i[1] for i in res]
        return res
        
