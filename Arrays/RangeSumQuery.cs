namespace Oops
{
    internal class RangeSumQuery
    {
        public List<long> RangeSum(List<int> A, List<List<int>> B)
        {
            int n = A.Count;
            var pf = new int[n];
            pf[0] = A[0];
            for (int i = 1; i < n; i++)
            {
                pf[i] = pf[i - 1] + A[i];
            }
            List<long> sums = new List<long>();
            for (int i = 0; i < B.Count; i++)
            {
                var s = B[i][0];
                var e = B[i][1];
                long sum;
                if (s == 1)
                {
                    sum = pf[e - 1];
                }
                else
                {
                    sum = pf[e - 1] - pf[s - 1 - 1];
                }
                sums.Add(sum);
            }
            return sums;
        }
    }
}
