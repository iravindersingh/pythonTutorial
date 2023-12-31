def longest_substring(str):
    longest_Sub = ""
    for j in range(len(str)):
        subsring = ""
        for i in range(j,len(str)):
            if(str[j] == str[i]):  #a /= b
                if(len(longest_Sub) < len(subsring)):
                    longest_Sub = subsring

                    subsring = ""
                # break
            subsring += str[i]

    print(longest_Sub)

str = "abcdabcbbxyzt"
longest_substring(str)



sub1 = "abcd"
sub2 = "bcbbxyzt"