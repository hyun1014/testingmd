<h1>Sorting coordinate</h1>
<hr>
<h2>Problem</h2><br>
There are N points above a 2-dimensional plane. Arrange coordinates in the order where x-coordinate increases. If there are points whose x-coordinate is the same for each other, arrange them in the order where y-coordinate increases. Write pseudo-code for solution.
<hr>
<h2>Algorithm hint</h2><br>
Use sorting algorithm. ex) Bubble sort, Selection sort, Merge sort, Quick sort, etc...
<hr>
~~~c++
    #include <iostream>
    #include <vector>
    #include <algorithm>

    using namespace std;

    bool comp(pair<int, int> a, pair<int, int> b) {
	    if (a.first == b.first)
		    return a.second < b.second;
    	else
	    	return a.first < b.first;
    }

    int main(void) {
	    int n;
	    scanf("%d", &n);
	    vector<pair<int, int>> v(n, make_pair(0,0));
	    for (int i = 0; i < n; i++)
		    scanf("%d %d", &v[i].first, &v[i].second);
	    sort(v.begin(), v.end(), comp);
	    for (int i = 0; i < n; i++)
	    	printf("%d %d\n", v[i].first, v[i].second);
	    return 0;
    }
~~~