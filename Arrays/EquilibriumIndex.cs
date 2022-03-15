namespace Oops
{
    internal class EquilibriumIndex
    {
        public int Solve(List<int> A)
        {
            var n = A.Count;
            int[] pf = new int[n];
            pf[0] = A[0];

            for (int i = 1; i < n; i++)
            {
                pf[i] = pf[i - 1] + A[i];
            }

            var index = -1;
            for (int i = 0; i < n; i++)
            {
                var left = 0;
                if (i != 0) left = pf[i - 1];

                var right = pf[n - 1] - pf[i];
                if (left == right)
                {
                    index = i;
                    break;
                }
            }
            return index;
        }
    }
}
