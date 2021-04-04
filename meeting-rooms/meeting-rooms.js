/**
 * @param {number[][]} intervals
 * @return {boolean}
 */
const canAttend = (intervals) => {
	intervals.sort(sortFunction);
  
  for (let i = 1; i < intervals.length; i++) {
  	if (intervals[i - 1][1] > intervals[i][0]) {
    	return false;
    }
  }
  return true;
}

var canAttendMeetings = function(intervals) {
      function sortFunction(a, b) {
      if (a[0] === b[0]) {
          return 0;
      }
      else {
          return (a[0] < b[0]) ? -1 : 1;
      }
  }
    
  intervals.sort(sortFunction);
  for (let i = 1; i < intervals.length; i++) {
  	if (intervals[i - 1][1] > intervals[i][0]) {
    	return false;
    }
  }
  return true;
};