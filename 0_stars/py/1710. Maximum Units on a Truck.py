# sort

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box = sorted(boxTypes, key=lambda x:x[1], reverse=True)

        cur_unit = 0
        cur_size = 0
        for box in sorted_box:
            if truckSize - cur_size >= box[0]:
                cur_unit += box[0]*box[1]
                cur_size += box[0]
            else:
                cur_unit += (truckSize - cur_size) * box[1]
                break
        return cur_unit 