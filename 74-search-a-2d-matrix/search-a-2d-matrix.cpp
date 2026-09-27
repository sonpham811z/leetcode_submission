class Solution {
public:
    bool binarySearch(vector<int>& row, int target)
    {
        int left = 0;
        int right = row.size()-1;
        
        while(left <= right)
        {
            int mid = (left+right)/2;

            if(row[mid] == target)
                return true;
            
            if(row[mid] > target)
                right = mid - 1;
            else
                left = mid+1;
        }

        return false;
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
         int row = matrix.size();
        int col = matrix[0].size();
        
        // Coi ma trận là mảng 1D có chỉ số từ 0 đến (row * col - 1)
        int left = 0;
        int right = row * col - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            // Quy đổi chỉ số mid 1D thành tọa độ [i][j] trong 2D
            int mid_val = matrix[mid / col][mid % col];
            
            if (mid_val == target) {
                return true;
            }
            if (mid_val < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return false;
    }
};