// Given two arrays that are sorted but not necessarily same length, find median value. Given ([1, 5, 9], [1, 2, 3, 4, 5, 6]), return 4. If number of values is even, return average of two middle values. Given ([1, 5, 9], [1, 2, 3, 4, 5, 6]), return 3.5.
function median_sorted_arr(arr1, arr2){
  var new_arr = arr1.concat(arr2).sort()
  if (new_arr.length % 2 == 1){
    mid_ind = Math.trunc(new_arr.length / 2);
    return new_arr[mid_ind];
  }
  else if (new_arr.length % 2 == 0){
    mid_ind1 = new_arr.length / 2;
    mid_ind2 = mid_ind1 - 1;
    return (new_arr[mid_ind1] + new_arr[mid_ind2]) / 2;
  }
}

var arr1 = [1, 5, 9];
var arr2 = [1, 2, 3, 4, 5, 6];
var arr3 = [1, 2, 3, 4, 5];

console.log(median_sorted_arr(arr1, arr2));
console.log(median_sorted_arr(arr1, arr3));
