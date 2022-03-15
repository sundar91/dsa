namespace Oops
{
    internal class PickFromBothSides
    {
        public int Solve(List<int> A, int B)
        {
            int currentSum = 0;
            for (int i = 0; i < B; i++)
            {
                currentSum += A[i];
            }
            
            var maxSum = currentSum;
            var exclude = B - 1;
            var include = A.Count - 1;
            for (int i = exclude, j = include; i >= 0 && j >= 0; i--, j--)
            {
                currentSum += A[j];
                currentSum -= A[i];
                maxSum = Math.Max(maxSum, currentSum);
            }
            return maxSum;
        }
    }
}
