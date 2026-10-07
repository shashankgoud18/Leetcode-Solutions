class Solution {
    public int maxArea(int[] arr) {
        int n = arr.length;
        int i = 0;
        int j = n - 1;
        int water = 0;

        while (i < j) {
            int small;

            if (arr[i] < arr[j])
                small = arr[i];
            else
                small = arr[j];

            int newWater = (j - i) * small;

            if (water < newWater)
                water = newWater;

            if (arr[i] < arr[j])
                i++;
            else
                j--;
        }

        return water;
    }
}

