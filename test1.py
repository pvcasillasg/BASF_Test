def longest_common_subsequence(str1, str2, str3):
    len1, len2, len3 = len(str1), len(str2), len(str3)
    
    dp = [[[0 for _ in range(len3 + 1)] for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            for k in range(1, len3 + 1):
                if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
    lcs_length = dp[len1][len2][len3]
    lcs = []
    i, j, k = len1, len2, len3
    while i > 0 and j > 0 and k > 0:
        if str1[i - 1] == str2[j - 1] == str3[k - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
            k -= 1
        elif dp[i - 1][j][k] >= dp[i][j - 1][k] and dp[i - 1][j][k] >= dp[i][j][k - 1]:
            i -= 1
        elif dp[i][j - 1][k] >= dp[i - 1][j][k] and dp[i][j - 1][k] >= dp[i][j][k - 1]:
            j -= 1
        else:
            k -= 1
    
    lcs.reverse()
    return ''.join(lcs)

sequence1 = "ADDB"
sequence2 = "CDDE"
sequence3 = "EDDF"
print(longest_common_subsequence(sequence1, sequence2, sequence3))

sequence1 = "UIBAZDBSIAHFB"
sequence2 = "PQACIZDBIBDLAG"
sequence3 = "QIDBCZDBKSHDVF"
print(longest_common_subsequence(sequence1, sequence2, sequence3))
