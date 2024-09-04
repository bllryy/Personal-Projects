#include <iostream> // group functions and variables together
using namespace std;

class FinsClass{
    public: 
        void coolText(){
            cout << "Hello World" << endl;
        }
};

int main()
{
    FinsClass FinsObject;
    FinsObject.coolText();

    return 0;
}