using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oops
{
    internal class EvenSumAndOddSum
    {
        /* Hint: after removing an element at any index the numbers index will change from even to odd and odd to even 
         * So even[i-1] + odd[n-1] - odd[i] sum of even number after removing an index at i */
        public int Solve(List<int> A)
        {
            var n = A.Count;
            var pfEven = new int[n];
            var pfOdd = new int[n];

            var even = 0;
            var odd = 0;

            for (int i = 0; i < n; i++)
            {
                if (i % 2 == 0)
                {
                    even += A[i];}
                else
                {
                    odd += A[i];
                }

                pfEven[i] = even;
                
                pfOdd[i] = odd;
            }
            int count = 0;

            for(int i = 0; i< n; i++)
            {
                var evenSum  = (i > 0 ? pfEven[i-1] : 0) + pfOdd[n-1] - pfOdd[i] ;
                var oddSum = (i > 0 ? pfOdd[i-1] : 0) + pfEven[n-1] - pfEven[i];

                if(evenSum == oddSum) count++;
            }

            return count;
        }
    }
}
