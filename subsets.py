import copy
class Solution:

    def subsets(self, nums: list[int]) -> list[list[int]]:

        '''
        For Loop Based Recursion : With backtracking

        TC: O(2^(n))
        AS: O(n)
        '''
        result = []
        N = len(nums)

        def helper(nums, pivot, path):

            # base logic
            ## add every node we will add the path
            result.append(copy.deepcopy(path))

            for i in range(pivot, len(nums)):

                ## ACTION 
                path.append(nums[i])

                ## RECURSE 
                helper(nums, i+1, path)

                ## BACKTRACK 
                path.pop()

        helper(nums, 0, [])
        return result


    # def subsets1(self, nums: list[int]) -> list[list[int]]:

    #     '''
    #     For Loop Based Recursion : Without backtracking, using Deepcopy

    #     TC: O(2^(n))
    #     AS: O(n)
    #     '''
    #     result = []
    #     N = len(nums)

    #     def helper(nums, pivot, path):

    #         # base logic
    #         ## add every node we will add the path
    #         result.append(path)

    #         for i in range(pivot, len(nums)):
    #             li = []
    #             li = copy.deepcopy(path)

    #             ## ACTION 
    #             li.append(nums[i])

    #             ## RECURSE 
    #             helper(nums, i+1, li)

    #     helper(nums, 0, [])
    #     return result


    # def subsets2(self, nums: list[int]) -> list[list[int]]:

    #     '''
    #     Without Recursion

    #     TC: O(2^(n))
    #     AS: O(1)
    #     '''
    #     result = []
    #     result.append([])

    #     for i in range(len(nums)):
    #         size = len(result) # result is mutating so never do for loop on a mutating result
    #         for j in range(size):
    #             li = []
    #             li = copy.deepcopy(result[j])
    #             li.append(nums[i])
    #             result.append(li)

    #     return result

    # def subsets3(self, nums: list[int]) -> list[list[int]]:

    #     '''
    #     0-1 Matrix : With backtracking

    #     TC: O(2^(n))
    #     AS: O(n)
    #     '''
    #     result = []
    #     N = len(nums)

    #     def helper(nums, idx, path):

    #         # base logic
    #         if idx == len(nums):
    #             result.append(copy.deepcopy(path))
    #             return

    #         ## ACTION 
    #         # not choose
    #         helper(nums, idx+1, path)

    #         ## RECURSE 
    #         # choose
    #         path.append(nums[idx])
    #         helper(nums, idx+1, path)

    #         ## BACKTRACK 
    #         path.pop()


    #     helper(nums, 0, [])
    #     return result
      
      
    # def subsets4(self, nums: list[int]) -> list[list[int]]:

    #     '''
    #     0-1 Matrix : With Deepcopy

    #     TC: O(2^(n))
    #     AS: O(n)
    #     '''
    #     result = []
    #     N = len(nums)

    #     def helper(nums, idx, path):

    #         # base logic
    #         if idx == len(nums):
    #             result.append(path)
    #             return

    #         ## ACTION 
    #         # not choose
    #         helper(nums, idx+1, copy.deepcopy(path))

    #         ## RECURSE 
    #         # choose
    #         path.append(nums[idx])
    #         helper(nums, idx+1, copy.deepcopy(path))

    #     helper(nums, 0, [])
    #     return result
            

if __name__ == "__main__":
    s = [1,2,3]
    sol = Solution()
    print("TEST CASE 1")
    print(sol.subsets(s))

    print("\n\n")

    s1 = [1,2,3,4]
    print("TEST CASE 2")
    print(sol.subsets(s1))