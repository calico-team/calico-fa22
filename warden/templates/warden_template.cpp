#include <iostream>

using namespace std;

double pulse(double xp, double yp);
void blast(double xb, double yb);

/**
 * Communicate with the judge using a series of pulse queries and blast queries.
 * Using P = 150 or fewer pulses, find Steve and blast them.
 * 
 * You can send queries by calling the pulse(double xp, double yp) and
 * blast(double xb, double yb) functions as defined below. If you miss your
 * blast, your program will exit.
 */
void solve() {
    // YOUR CODE HERE
    return;
}

double pulse(double xp, double yp) {
    cout << "P " << xp << " " << yp << endl;
    string response;
    cin >> response;
    if (response == "WRONG_ANSWER") {
        exit(0);
    }
    return stod(response);
}

void blast(double xb, double yb) {
    cout << "B " << xb << " " << yb << endl;
    string response;
    cin >> response;
    if (response == "WRONG_ANSWER") {
        exit(0);
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        solve();
    }
}
