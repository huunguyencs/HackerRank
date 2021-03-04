#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {
    int len = s.length();
    long numLoop = n / len;
    int remainder = n % len;

    int numOfA = 0;
    int numOfARemainder = 0;
    for(int i = 0; i < len; i++){
        if(s[i] == 'a'){
            numOfA++;
            if(i < remainder){
                numOfARemainder++;
            }
        }
    }
    return long(numLoop*numOfA + numOfARemainder);
}

int main()
{
    // ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    // fout << result << "\n";

    // fout.close();
    cout << result << "\n";

    return 0;
}