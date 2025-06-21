import copy

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        FOR LOOP BASED: With Backtracking
        TC: O(2^n)
        AS: O(n)
        """

        result = []
        N = len(s)

        def helper(s, pivot, path):

            # Base case
            if pivot == len(s): # pivot goes out of bound
                result.append(copy.deepcopy(path))

            for i in range(pivot, len(s)):
                currSplit = s[pivot:i+1]

                # ACTION
                if currSplit == currSplit[::-1]:
                    path.append(currSplit)

                    # RECURSE
                    helper(s, i+1, path)

                    # BACKTRACK
                    path.pop()
                
        helper(s, 0, [])
        return result


    # def partition2(self, s: str) -> list[list[str]]:
    #     """
    #     FOR LOOP BASED: Without Backtracking, using deepcopy
    #     TC: O(2^n)
    #     AS: O(n)
    #     """

    #     result = []
    #     N = len(s)

    #     def helper(s, pivot, path):

    #         # Base case
    #         if pivot == len(s): # pivot goes out of bound
    #             result.append(path)

    #         for i in range(pivot, len(s)):
    #             currSplit = s[pivot:i+1]

    #             # ACTION
    #             if currSplit == currSplit[::-1]:
    #                 li = []
    #                 li = copy.deepcopy(path)
    #                 li.append(currSplit)

    #                 # RECURSE
    #                 helper(s, i+1, li)
        
    #     helper(s, 0, [])
    #     return result

if __name__ == "__main__":
    s = "aab"
    sol = Solution()
    print("TEST CASE 1")
    print(sol.partition(s))

    print("\n\n")

    s1 = "aaba"
    print("TEST CASE 2")
    print(sol.partition(s1))
