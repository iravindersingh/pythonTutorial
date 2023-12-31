

def longest_substring(str):
    left =0
    right = 0
    maxString = set()
    maxWindow = 0

    while(right < len(str)):
        c= str[right]
        if(maxString.add(c)):
            right += 1
            maxWindow = max(maxWindow,right - left +1)
            print(right)
        else:
            while str[left] != c:
                maxString.remove(str[left])
                left +=1
            maxString.remove(c)
            print(left)


longest_substring("sdfghasdesrtfyadsa")