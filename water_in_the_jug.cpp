#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canMeasureWater(int x, int y, int target) {
        // Target cannot exceed the total capacity
        if (target > x + y)
            return false;

        // If one jug is empty, target must be zero
        if (target == 0)
            return true;

        // A target is possible iff it is divisible by gcd(x, y)
        return target % gcd(x, y) == 0;
    }
};
