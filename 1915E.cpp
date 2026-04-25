// E. Romantic Glasses
// https://codeforces.com/problemset/problem/1915/E
// rating: 1300

#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;

    while (t--){
        int n;
        cin >> n;

        vector<long long> a(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }

        set<long long> prefix;
        prefix.insert(0);

        long long curSum = 0;
        bool found = false;

        for (int i  = 0; i < n; i++){
            if (i % 2 == 0){
                curSum += a[i];
            }else{
                curSum -= a[i];
            }

            if (prefix.count(curSum) == 1){
                found = true;
                break;
            }

            prefix.insert(curSum);
        }

        if (found){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
        
    }
}