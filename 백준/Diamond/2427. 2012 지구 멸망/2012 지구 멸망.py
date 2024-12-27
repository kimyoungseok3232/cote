import sys
import math
N, P, V = map(int, sys.stdin.readline().rstrip().split())
min_value = math.inf
pin_list = [N]
yet_dict = {}
i = -1
if N == 1:
    print(0)
else:
    while 1:
        i += 1
        if i in yet_dict:
            value = yet_dict.pop(i)
            if value == 1:
                print(i)
                break
            if min_value > value:
                min_value = value
            pin_list.append(value)
        while pin_list:
            a = pin_list.pop()
            tmp1 = 0
            tmp3 = 0
            while 1:
                tmp1 += 1
                tmp2 = math.ceil(a**(1/tmp1))
                if tmp2 == tmp3:
                    if tmp2 == 2:
                        break
                    continue
                tmp3 = tmp2
                key = i + tmp2 * P + V
                value = math.ceil(a/tmp2)
                if min_value < value:
                    continue
                if key in yet_dict:
                    if yet_dict[key] > value:
                        yet_dict[key] = value
                else:
                    yet_dict[key] = value