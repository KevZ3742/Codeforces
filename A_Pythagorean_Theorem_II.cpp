#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    int counter = 0;
    for (int a = 1; a <= n; a++){
        for (int b = a; b <= n; b ++){
            int c2 = a * a + b * b;
            int c = sqrt(c2);

            if (c2 == c * c and c <= n){
                counter++;
            }
        }
    }

    cout << counter << "\n";
}