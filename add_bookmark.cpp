#include <vector>
#include <string>
#include <fstream>

using namespace std;
using std::endl;

class Bookmark {
private:
    string subject;
    string url;
public:
    Bookmark(string topic, string link) {
        subject = topic;
        url = link;
    }

    string getSubject() {
        return subject;
    }
    string getURL() {
        return url;
    }

    // Overloaded operators for comparing
    bool operator > (const Bookmark &compare) const {
        return this->subject > compare.subject;
    }
    bool operator >= (const Bookmark &compare) const {
        return this->subject >= compare.subject;
    }
    bool operator < (const Bookmark &compare) const {
        return this->subject < compare.subject;
    }
    bool operator <= (const Bookmark &compare) const {
        return this->subject <= compare.subject;
    }
};

void bubble_sort(vector<Bookmark> vec) {
    bool haveSwapped = true;
    int maxIndex = vec.size();
    while (haveSwapped) {
        haveSwapped = false;
        for (int i = 0; i + 1 < maxIndex; ++i) {
            // Compare items at indices i and i+1 and swap if necessary
            if (vec[i] > vec[i+1]) {
                Bookmark temp = vec[i];
                vec[i] = vec[i+1];
                vec[i+1] = temp;
                // Update haveSwapped
                haveSwapped = true;
            }
        }
        --maxIndex; // Update maxIndex
    }
}

int main(int argc, char* argv[]) {
    string topic = argv[1];
    string link = argv[2];

    vector<Bookmark> bookmarks;

    // Read in data from bookmark file
    ifstream fIn;
    fIn.open("bookmarks.txt");

    // Declares the variables to be read in
    string bookmark_topic;
    string bookmark_link;

    //Loops through all the data
    while (fIn && fIn.peek() != EOF) {
        getline(fIn, bookmark_topic);
        getline(fIn, bookmark_link);

        bookmarks.push_back(Bookmark(bookmark_topic, bookmark_link));
    }
    fIn.close();

    //Add the new bookmark to the list
    bookmarks.push_back(Bookmark(topic, link));

    for (int i = 0; i < bookmarks.size(); ++i) {
        system(("echo " + bookmarks[i].getSubject()).c_str());
    }
    // Sort alphabetically using bubble sort
    bubble_sort(bookmarks);

    for (int i = 0; i < bookmarks.size(); ++i) {
        system(("echo " + bookmarks[i].getSubject()).c_str());
    }

    // Print output to txt file
    ofstream fOut;
    fOut.open("bookmarks.txt");

    // Write to output file
    for (int i = 0; i < bookmarks.size(); ++i) {
        fOut << bookmarks[i].getSubject() << endl;
        // The last bookmark doesn't add a new line character so the formatting doesn't get messed up
        if (i < bookmarks.size() - 1) {
            fOut << bookmarks[i].getURL() << endl;
        }
        else fOut << bookmarks[i].getURL();
    }
    fOut.close();

    return 0;
}