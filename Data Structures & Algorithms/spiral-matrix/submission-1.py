class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        ans = []
        i,j = 0,0
        u,r,d,l = 0,1,2,3
        dire = r
        u_w = 0
        r_w = n
        d_w = m
        l_w = -1
        while len(ans) != m * n:
            if dire == r:
                while j < r_w:
                    ans.append(matrix[i][j])
                    j += 1
                i,j = i+1,j-1
                r_w -= 1
                dire = d
            elif dire == d:
                while i < d_w:
                    ans.append(matrix[i][j])
                    i += 1
                i,j = i - 1 , j - 1
                d_w -= 1
                dire = l
            elif dire == l :
                while j > l_w:
                    ans.append(matrix[i][j])
                    j -= 1
                i,j = i - 1 , j + 1
                l_w += 1
                dire = u
            else:
                while i > u_w:
                    ans.append(matrix[i][j])
                    i -= 1
                i,j = i + 1 , j + 1
                u_w += 1
                dire = r
        return ans