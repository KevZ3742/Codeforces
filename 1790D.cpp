// D. Matryoshkas
// https://codeforces.com/problemset/problem/1790/D
// rating: 1200

#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;

        vector<int> a(n);
        map<int, int> counter;

        for(int i = 0; i < n; ++i){
            cin >> a[i];
            counter[a[i]]++;
        }

        int toPrint = 0;
        for(auto& [num, freq] : counter){
            int prevFreq = counter.count(num - 1) ? counter[num - 1] : 0;
            toPrint += max(0, freq - prevFreq);
        }

        cout << toPrint << "\n";
    }
}