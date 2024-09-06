#include <iostream>
#include <vector>
#include <utility> // Needed for std::pair

using namespace std;

// Define the bounds for each variable
vector<pair<int, int>> bounds = {
    {2008, 67434882}, {5828, 35387831}, {2933, 30133881}, {411, 63609725},
    {4223, 18566959}, {1614, 25526751}, {5679, 44298843}, {6349, 26793895},
    {117, 40292840}, {2321, 42293336}, {2281, 26301527}, {1939, 50793633},
    {6273, 51546489}, {1477, 36871159}, {800, 65314188}, {4727, 15882817},
    {2828, 40562779}, {1782, 48186923}, {1744, 37382713}, {2486, 56149154},
    {6312, 18170199}, {2188, 63940428}, {5380, 58244044}, {1772, 29193116},
    {2708, 22309445}, {1528, 40848052}
};

// Calculate the number of solutions using stars and bars
long long stars_and_bars(int n, int k) {
    if (k < 0 || n < 0)
        return 0;
    else if (k == 0 || n == 0)
        return 1;
    else
        return stars_and_bars(n - 1, k - 1) + stars_and_bars(n - 1, k);
}

int main() {
    // Calculate the total number of solutions
    long long total_solutions = stars_and_bars(69696969 + 26 - 1, 26);

    // Calculate the remainder when the total number of solutions is divided by 69696969
    long long remainder = total_solutions % 69696969;

    cout << "Flag: BITSCTF{" << remainder << "}" << endl;

    return 0;
}
