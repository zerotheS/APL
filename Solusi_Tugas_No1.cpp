#include <iostream>
using namespace std;

int main()
{
    int a,b,c;
    cout<<"Kelompok 18 APL"<<endl;
    cout<<"       **    "<<endl;
    cout<<"      ****    "<<endl;
    cout<<" A   ******  B "<<endl;
    cout<<"    ********    "<<endl;
    cout<<"   **********    "<<endl;
    cout<<"  ************    "<<endl;
    cout<<"        C          "<<endl;
    cout <<"Berikan sisi A : ";
    cin >> a;

    cout <<"Berikan sisi B : ";
    cin >> b;

    cout <<"Berikan sisi C : ";
    cin >> c;
    int d;
    d = a,b,c;
    if(d!=0){
        if(a==b && a==c)
        {
        cout<<"Segitiga sama sisi"<<endl;
        }
        else if(a==b || a==c || b==c)
        {
        cout<<"Segitiga sama kaki"<<endl;
        }
        else if(a*a==b*b+c*c||b*b==a*a+c*c||c*c==a*a+b*b){
            cout<<"Segitiga Siku-Siku"<<endl;
        }
        else {
        cout<<"Segitiga sembarang"<<endl;
        }
        }
    else {
        cout<<"Bukan segitiga"<<endl;
        }


    system("pause");
    return 0;

}