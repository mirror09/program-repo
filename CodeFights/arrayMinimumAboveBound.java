int arrayMinimumAboveBound(int[] inputArray, int bound) {

  int best = -1;
  for (int i = 0; i < inputArray.length; i++) {
    if (inputArray[i] > bound && 
        (best == -1 || inputArray[i] < best)) {
      best = inputArray[i];
    }
  }

  return best;
}
