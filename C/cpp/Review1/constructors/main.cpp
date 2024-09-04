#include <iostream>
#include <string> // text/name
using namespace std;

class FinsClass{
    public: // constructor
        FinsClass(string y){
            setName(y);
        }
        void setName(string x){     // change the name 
            name = x;
        }
        string getName(){           // get the name... duh
            return name;
        }
    private:
        string name;
};


// below is the way it was written before, but now we can just call FinsClass Fo.....
//int main()
//{
  //  FinsClass Fo;               // obj
    //Fo.setName("Hello World!"); // obj seperator function
    //cout << Fo.getName();
    //return 0;
//}

int main()
{
    FinsClass Fo("Hello World!!!");
    cout << Fo.getName();

    FinsClass Fo2(" Hello 2??");
    cout << Fo2.getName();
    return 0;
}