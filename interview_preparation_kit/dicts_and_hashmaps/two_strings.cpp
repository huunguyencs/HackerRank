#include <bits/stdc++.h>

using namespace std;

// Complete the twoStrings function below.
string twoStrings(string s1, string s2) {
    map<char, int> m1;
    map<char, int> m2;

    for (int i = 0; i < s1.length(); i++){
        try {
            m1[s1[i]]++;
        }
        catch(exception e){
            m1[s1[i]] = 1;
        }
    }

    for (int i = 0; i < s2.length(); i++){
        try {
            m2[s2[i]]++;
        }
        catch(exception e){
            m2[s2[i]] = 1;
        }
    }

    map<char, int>::iterator it1;
    for(it1 = m1.begin(); it1 != m1.end(); it1++){
        map<char, int>::iterator it2 = m2.find(it1->first);
        if(it2 != m2.end())
            return "YES";
    }

    return "NO";
}

int main()
{
    // ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s1;
        getline(cin, s1);

        string s2;
        getline(cin, s2);

        string result = twoStrings(s1, s2);

        // fout << result << "\n";
        cout << result << "\n";
    }

    // fout.close();

    return 0;
}
