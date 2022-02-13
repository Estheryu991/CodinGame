import sys
import math

n = int(input())
for i in range(n):
    x = int(input())
    if x %2 == 0: 
        print("true")
    else: 
        print("false")
        
  return new AbstractIterator<Integer>() {
  int next = getStart();

  @Override protected Integer computeNext() {
    if (isBeyondEnd(next)) {
      return endOfData();
    }
    Integer result = next;
    next = next + getStep();
    return result;
  }
};
