#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);


void swap_arr(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}

// Complete the minimumSwaps function below.
int minimumSwaps(vector<int> arr) {
    int countSwap = 0;
    int i = 0;
    while(i < arr.size()){
        int j = arr[i];
        if(i + 1 != j){
            swap_arr(arr[i], arr[j - 1]);
            countSwap++;
        }
        else i++;
    }
    return countSwap;
}



int main()
{
    // ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int res = minimumSwaps(arr);

    // fout << res << "\n";

    // fout.close();
    cout << res << "\n";

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
