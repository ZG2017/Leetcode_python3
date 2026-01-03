# from sx/sy to tx/ty is hard to solve, but from tx/ty to sx/sy is easy to solve.

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        def compute_c(cur_max_one, cur_min_one, buttom_value):
            return math.floor((cur_max_one - buttom_value)/cur_min_one)

        cur_tx, cur_ty = tx, ty
        while cur_tx >= sx and cur_ty >= sy:
            if cur_tx == sx and cur_ty == sy:
                return True
            if cur_tx == cur_ty:
                if cur_tx == sx and cur_ty == sy:
                    return True
                else:
                    return False
            elif cur_tx > cur_ty:
                # get offset coif
                c = compute_c(cur_tx, cur_ty, sx)
                if c == 0:
                    return False
                cur_tx = cur_tx - cur_ty * c
            else:
                c = compute_c(cur_ty, cur_tx, sy)
                if c == 0:
                    return False
                cur_ty = cur_ty - cur_tx * c
        return False


# update solution
# https://leetcode.com/problems/reaching-points/solutions/5332350/only-solution-youll-need-0ms100-faster-e-xttl/

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while (tx>=sx and ty>=sy):
            if tx==sx:
                return (ty-sy)%tx==0
            if ty==sy:
                return (tx-sx)%ty==0
            if ty>tx:
                ty=ty%tx
            else:
                tx=tx%ty
        return False