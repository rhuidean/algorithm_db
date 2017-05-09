// Given an integer representing number of minutes elapsed since midnight, return a string representing current time, in traditional spoken convention. User numerals, except specifically following words - midnight, noon, past, til, half, quarter. Examples: given 30, return "half past midnight"; given 75, return "quarter past 1 am"; given 710, return "10 til noon"; given 1000, return "20 til 5 pm".
var time_to_eng = (min) => {
  var words_arr = ["midnight", "noon", "past", "til", "half", "quarter"];
  var first_wrd, sec_wrd;
  var time_hr = Math.trunc(min / 60);
  var time_min = (min/60 - Math.trunc(min / 60)) * 60;

  if (time_min == 15) {
    first_wrd = words_arr[5];
    sec_wrd = words_arr[2];
  }
  else if (time_min == 30) {
    first_wrd = words_arr[4];
    sec_wrd = words_arr[2];
  }
  else if (time_min == 45) {
    first_wrd = words_arr[5];
    sec_wrd = words_arr[3];
    time_hr = Math.ceil(min / 60);
  }
  else if (time_min > 30) {
    first_wrd = Math.round(60 - time_min);
    sec_wrd = words_arr[3];
    time_hr = Math.ceil(min / 60);
  }
  else if (time_min < 30) {
    sec_wrd = words_arr[2];
  }
  if (time_hr == 0) {
    third_wrd = words_arr[0];
  }
  else if (0 < time_hr && time_hr < 12) {
    third_wrd = time_hr + " am";
  }
  else if (time_hr == 12) {
    third_wrd = words_arr[1];
  }
  else if (12 < time_hr && time_hr < 24) {
    third_wrd = (time_hr - 12) + " pm";
  }

  return first_wrd + " " + sec_wrd + " " + third_wrd;
}

console.log(time_to_eng(30));
console.log(time_to_eng(75));
console.log(time_to_eng(710));
console.log(time_to_eng(1000));
