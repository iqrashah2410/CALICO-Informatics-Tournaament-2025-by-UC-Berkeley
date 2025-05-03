#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        string s;
        getline(cin, s);
        long long ans = 0, totalU = 0, uBeforeLastW = 0;
        for (char c : s) {
            if (c == 'w') uBeforeLastW = totalU;
            else if (c == 'u') {
                ans += uBeforeLastW;
                totalU++;
            }
        }
        cout << ans << '\n';
    }
    return 0;
}
