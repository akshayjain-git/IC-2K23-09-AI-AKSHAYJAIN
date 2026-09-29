#include <iostream>
using namespace std;

// Function to maximize
int f(int x) {
    return -(x - 5) * (x - 5) + 25;
}

int hillClimbing(int start, int step) {
    int current = start;

    while (true) {
        int next = current + step;

        // If the neighboring state is better, move to it
        if (f(next) > f(current)) {
            current = next;
        }
        else {
            // No better neighbor found
            break;
        }
    }

    return current;
}

int main() {
    int start, step;

    cout << "Enter starting point: ";
    cin >> start;

    cout << "Enter step size: ";
    cin >> step;

    int result = hillClimbing(start, step);

    cout << "Maximum value found at x = " << result << endl;
    cout << "Function value = " << f(result) << endl;

    return 0;
}
