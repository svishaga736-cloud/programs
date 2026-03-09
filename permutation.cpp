class Solution {
public:
    void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
        // Base case: if we've reached the end of the array, we found a permutation
        if (start == nums.size()) {
            result.push_back(nums);
            return;
        }

        for (int i = start; i < nums.size(); ++i) {
            // Swap current element with the element at index 'i'
            swap(nums[start], nums[i]);
            
            // Recurse to fill the next position
            backtrack(nums, start + 1, result);
            
            // Backtrack: swap back to restore the original array for the next iteration
            swap(nums[start], nums[i]);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(nums, 0, result);
        return result;
    }
};
