#include <iostream>
#include <string> // text/name
using namespace std;

class FinsClass{
    public:
        void setName(string x){     // change the name 
            name = x;
        }
        string getName(){           // get the name... duh
            return name;
        }
    private:
        string name;
};

int main()
{
    FinsClass Fo;               // obj
    Fo.setName("Hello World!"); // obj seperator function
    cout << Fo.getName();
    return 0;
}