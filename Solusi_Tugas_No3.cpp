#include <iostream>
using namespace std;

long int pangkatrekursif(int a, int b);

int main(){
	
	int a,b;
	
	cout<<"FUNGSI REKURSIF UNTUK MENGHITUNG PANGKAT"<<endl;
	cout<<endl;
	cout<<"Masukkan nilai a = ";
	cin>>a;
	
	cout<<"Masukkan pangkat dari nilai a = ";
	cin>>b;
	cout<<endl;
	cout<<a<<" pangkat "<<b<<" = "<<pangkatrekursif(a,b)<<endl;
}


long int pangkatrekursif(int a, int b){
	if (b==0)
	return 1 ;
	else 
                 return a * pangkatrekursif(a,b-1);
} 