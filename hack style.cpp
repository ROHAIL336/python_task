#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <algorithm>
#include <cctype>
using namespace std;

// Helper to strip punctuation and convert a word to lowercase
string cleanWord(const string& raw) {
    string cleaned = "";
    for (char ch : raw) 
	{
        if (isalnum(static_cast<unsigned char>(ch))) 
		{
            cleaned +=tolower(static_cast<unsigned char>(ch));
        }
    }
    return cleaned;
}

int main()
 {
    // Fast I/O standard in competitive programming
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string sentence;
    if (!getline(cin, sentence)) {
        return 0;
    }

    // 1. Core: Tokenize and populate hash map
    unordered_map<string, int> freqMap;
    stringstream ss(sentence);
    string token;

    while (ss >> token) {
        string word = cleanWord(token);
        if (!word.empty())
		{
            freqMap[word]++;
        }
    }

    cout << "--- Core: Word Counts ---\n";
    for (const auto& entry : freqMap) {
        cout << entry.first << ": " << entry.second << "\n";
    }

    // 2. Stretch: Extract to a vector and sort
    vector<pair<string, int>> wordList(freqMap.begin(), freqMap.end());

    // Sort: Higher count first; if tied, alphabetical order
    sort(wordList.begin(), wordList.end(), 
        [](const pair<string, int>& a, const pair<string, int>& b) {
            if (a.second != b.second) {
                return a.second > b.second; // Descending by frequency
            }
            return a.first < b.first;       // Ascending alphabetically
        }
    );
    cout << "\n--- Stretch: Top 3 Most Frequent ---\n";
    int limit = min(3, static_cast<int>(wordList.size()));
    for (int i = 0; i < limit; ++i) {
        cout << wordList[i].first << ": " << wordList[i].second << "\n";
    }

    return 0;
}
