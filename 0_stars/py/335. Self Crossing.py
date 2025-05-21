# mine:
class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) <= 3:
            return False
        vertical = []  # (horizental position,(from,to))
        horizental = []  # (vertical position,(from,to))
        curr_point = (0,0)
        for i in range(len(x)):
            last_point = curr_point
            if i%4 == 0:
                curr_segment = (curr_point,(curr_point[0],curr_point[1]+x[i]))
                curr_point = curr_segment[1]
            elif i%4 == 1:
                curr_segment = ((curr_point[0]-x[i],curr_point[1]),curr_point)
                curr_point = curr_segment[0]
            elif i%4 == 2:
                curr_segment = ((curr_point[0],curr_point[1]-x[i]),curr_point)
                curr_point = curr_segment[0]
            elif i%4 == 3:
                curr_segment = (curr_point,(curr_point[0]+x[i],curr_point[1]))
                curr_point = curr_segment[1]
            if i%2 == 0:
                lower = 0
                higher = len(horizental)-1
                while higher >= lower:
                    mid = int((lower+higher)/2)
                    if horizental[mid][0] < curr_segment[0][1]:
                        lower = mid + 1
                    else:
                        higher = mid - 1
                index = lower
                while index < len(horizental) and horizental[index][0] <= curr_segment[1][1]:
                    if horizental[index][1][0] <= curr_segment[0][0] <= horizental[index][1][1] and\
                    (curr_segment[0][0],horizental[index][0]) != last_point:
                        return True
                    index += 1
                lower = 0
                higher = len(vertical)-1
                while higher >= lower:
                    mid = int((lower+higher)/2)
                    if vertical[mid][0] < curr_segment[0][0]:
                        lower = mid + 1
                    else:
                        higher = mid - 1
                while lower < len(vertical) and vertical[lower][0] == curr_segment[0][0]:
                    if curr_segment[0][1] > vertical[lower][1][1] or curr_segment[1][1] < vertical[lower][1][0]:
                        lower += 1
                        continue
                    else:
                        return True
                vertical.insert(lower,(curr_segment[0][0],(curr_segment[0][1],curr_segment[1][1])))
            else:
                lower = 0
                higher = len(vertical)-1
                while higher >= lower:
                    mid = int((lower+higher)/2)
                    if vertical[mid][0] < curr_segment[0][0]:
                        lower = mid + 1
                    else:
                        higher = mid - 1
                index = lower
                while index < len(vertical) and vertical[index][0] <= curr_segment[1][0]:
                    if vertical[index][1][0] <= curr_segment[0][1] <= vertical[index][1][1] and \
                    (vertical[index][0],curr_segment[0][1]) != last_point:
                        return True
                    index += 1
                lower = 0
                higher = len(horizental)-1
                while higher >= lower:
                    mid = int((lower+higher)/2)
                    if horizental[mid][0] < curr_segment[0][1]:
                        lower = mid + 1
                    else:
                        higher = mid - 1
                while lower < len(horizental) and horizental[lower][0] == curr_segment[0][1]:
                    if curr_segment[0][0] > horizental[lower][1][1] or curr_segment[1][0] < horizental[lower][1][0]:
                        lower += 1
                        continue
                    else:
                        return True
                horizental.insert(lower,(curr_segment[0][1],(curr_segment[0][0],curr_segment[1][0])))
        return False



# updated: (clever)
class Solution:
    #                c                                        e
    #   +----------------+             +----------------+
    #   |                          |             |                          |
    #   |                          |             |                          | f
    # b|                          |          d |                          |
    #   |                          | d          |                          |    a
    #   +----------->      |             |                          | <--+
    #            a                |             |                          |       | b
    #                              |             |                                  |
    #                                           +-----------------------+
				c
class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c - e >= 0 and f >= d - b):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False
