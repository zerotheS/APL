#include <iostream>
using namespace std;

int main() {
    int x, y, z[5][5];
    for (x=0;x<5;x++){
        for (y=0;y<5;y++){
            if (x==y)
                z[x][y]=0;
            else if (x==2 and y==1)
                z[x][y]=8;
            else if (x==3 and y==1)
                z[x][y]=8;
            else if (x==3 and y==2)
                z[x][y]=8;
            else if (x==4)
                z[x][y]=8;
            else if (y==0)
                z[x][y]=8;
            else
                z[x][y]=7;
            cout << " ";
            cout << z[x][y];
            cout << "  ";
            }
    cout << "\n";
    }
}