# after getting value to idx_list, we can summary the formula to get the sum of distance gap.
class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        dict_holder = dict()
        for idx, i in enumerate(arr):
            if i not in dict_holder:
                dict_holder[i] = []
            dict_holder[i].append(idx)
        
        # print(dict_holder)
        
        sum_started_right = dict()
        neg_sum_strated_left = dict()
        for i, cur_list in dict_holder.items():
            cur_neg_sum = 0
            neg_sum_strated_left[i] = [0]
            for j in cur_list:
                cur_neg_sum -= j
                neg_sum_strated_left[i].append(cur_neg_sum)
            
            cur_sum = 0
            sum_started_right[i] = [0]
            for j in cur_list[::-1]:
                cur_sum += j
                sum_started_right[i].append(cur_sum)
            sum_started_right[i] = sum_started_right[i][::-1]

        ans_dict = dict()
        
        for i, cur_list in dict_holder.items():
            cur_len = len(cur_list)
            ans_dict[i] = []
            for idx, j in enumerate(cur_list):
                left_hand_side = neg_sum_strated_left[i][idx]
                right_hand_side = sum_started_right[i][idx+1]
                cur_tmp = j * (idx) - j * (cur_len - idx - 1)
                # print(i, idx)
                # print(neg_sum_strated_left[i])
                # print(sum_started_right[i])
                # print(left_hand_side, right_hand_side, cur_tmp, abs(left_hand_side + right_hand_side + cur_tmp))
                # print('--------------')
                ans_dict[i].append(abs(left_hand_side + right_hand_side + cur_tmp))
            ans_dict[i] = ans_dict[i]
        
        ans = [0] * len(arr)
        for i, idx_list in dict_holder.items():
            for idx, j in enumerate(idx_list):
                ans[j] = ans_dict[i][idx]
        return ans