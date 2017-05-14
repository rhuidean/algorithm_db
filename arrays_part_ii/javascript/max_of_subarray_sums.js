// Page 91. Given a numerical array that is potentially very long, return max sum of values from a subarray. Any consecutive sequence of indices in arrary is considered a subarray. Create a function that returns highest sum possible from these subarrays. Given [1, 2, -4, 3, -2, 3, -1], return 4 (from subarray [3, -2, 3]). Given [-1, -2, -4, -3, -2, -3], return 0 (for []).
var maxSubarrSum = (arr) => {
  var sum = 0, max = 0;
  for (let i = 0; i < arr.length; i++) {
    if (sum + arr[i] > 0) {
      sum += arr[i];
      if (sum > max) {
        max = sum;
      }
      console.log("Max:", max);
      console.log("Sum:", sum);
    }
    else {
      sum = 0;
      console.log("Max:", max);
      console.log("Sum:", sum);
    }
  }
  return max;
}

arr1 = [1, 2, -4, 3, -2, 3, -1];
arr2 = [-1, -2, -4, -3, -2, -3];
console.log(maxSubarrSum(arr1));
console.log(maxSubarrSum(arr2));
