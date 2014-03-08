Recently I came across a problem that required me to iterate through an ordered array of integers, sort them into different buckets and give an count of the bucket sizes as the output.

Here's an example input: 

	int a[] = {653, 444, 231, 120, 98, 88, 43, 12, 9, 3, 1};
	
at the first glance this looks exactly like a divide and conquer problem, and it is. Let's give a better description of the problem and try to break it down into subproblems.

Essentially, I want to know how many integers in the above **sorted** array are *larger* than some arbitrary given values.

for example, if my inputs are *130*, *65*, and *10*,
I would get the output 3, 6, and 8. To make it pretty, we can output it nicely:
	
	{"130": 3, "65": 6, "10": 8}
	
since the input can be arbitrary, the above keys are too.

before we attempt to do anything, can we write a naive solution to this problem? Let's try it in Python:

	def partition(seq, cond):
		d = defaultdict(int)
		for v in seq:
			for c in cond:
				if v > c:
					d[cond] += 1
		return d
		
what's the runtime on this piece of code? you can tell simply by inspection that the best and worst cases are both O(n), where *n* is the length of input *seq*. We need to traverse through the entire input to check and 'partition' the values. The eventual runtime, with *m* partitions, would be **m*O(n)**, in other words, not very good.

now let's break down the problem, can we do better? Let's assume yes (and yes we can!).

a very crucial piece of observation (give yourself a pat on the back if you know what it is!) is the fact that the partition size is closely related to the index location of the search values the partitions are based on. 

to put it simply, instead of a "counting" problem, let's look at it another way, let's look at it as a search problem.

for example, using the same input "a" above, if we want to find the number of elements in the array that's larger than *130*, we just need to insert it into the array correctly in sorted order, and return it's index. In this case, it would be at index 3, which matches exactly to the number of elements larger than it! This works for *65* as well, we should insert it at i=6 and so on.

of course, this only works if the array is sorted. do we know any search algorithm that works only on sorted arrays?

binary search comes to mind, from algorithms 101 we know that it runs with a running time of O(log(n)), an improvement from O(n).

So let's write a binary search that takes an array of defending integers, an integer to partition the array on, and a starting and end index.

	int binary_search(int lookfor, int a[], int start, int end) {
	    if (end == start) {
	        return start - 1;
	    }
	    if (end - start == 1) {
	        if (a[start] >= lookfor) {
	            return start;
	        }
	        return start - 1;
	    }
	
	    int mid = (start + end)/2;
	    int mid_val = a[mid];
	
	    if (mid_val == lookfor) {
	        return mid;
	    } else if (lookfor < mid_val) {
	        return binary_search(lookfor, a, mid + 1, end);
	    } else {
	        return binary_search(lookfor, a, start, mid);
	    }
	}

the correctness of the above algorithm is fairly evident, the two base cases take care of input array size of 1 and 2 element respectively, and the rest is a recursive call to itself, breaking the problem down into subproblems of size = size / 2

so what is the point of all this? what is the real world application?

the problem that I came across was that I had an input array of thousands of unix timestamps, I needed to quickly parse those timestamps into buckets of time ranges, i.e. 2h ago, 4h ago, 8h ago and 12h ago.

the naive solution is to traverse the array of timestamps and compare to the timestamp that corresponds to the cut off of each period (i.e. NOW - (2 * 60 * 60) would be the cut off for 2h), but the better solution is to use binary search to look for where that cutoff timestamp would fall in the sorted array.

this furthers saves me execution time as I can use the return value for 2h ago as the starting point (parameter start) for 4h, because I know that everything that's within 2h is also within 4h, and so on.

the benchmark on execution time also confirms my implementation, with an array size of 1800 timestamps, using the naive method takes **7675**us where the binary search method takes **270**us. That's a 30x improvement!









 
