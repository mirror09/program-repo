/* Given array of integers, find the maximal possible sum of some of 
 * its k consecutive elements.
 * 
 * for array = [2, 3, 5, 1, 6], k = 2 output should be 8
 * https://codefights.com/task/mwfCpXQL3kbJS4mm7
 * 
 * 
 */

int arrayMaxConsecutiveSum(int[] inputArray, int k) {

  int result = 0,
      currentSum = 0;

  for (int i = 0; i < k - 1; i++) {
    currentSum += inputArray[i];
  }
  for (int i = k - 1; i < inputArray.length; i++) {
    currentSum += inputArray[i];
    if (currentSum > result) {
      result =  currentSum ;
    }
    currentSum -= inputArray[i - k + 1];
  }

  return result;
}
