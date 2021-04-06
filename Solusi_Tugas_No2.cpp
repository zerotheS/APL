#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	cout << "Kelompok 18 APL"<< endl;
	cout << "Program Menghitung Nilai Pythagoras" << endl;
	int a,b,c;
	cout << "Masukkan Nilai sisi a: ";
	cin >> a;
	cout << "Masukkan Nilai sisi b: ";
	cin >> b;
	cout << "Masukkan Nilai sisi c: ";
	cin >> c;
	int st,sm;
	if (b , c < a){
		st = a;
		sm = sqrt(b*b + c*c);}
	else if (a , c < b){
		st = b;
		sm = sqrt(a*a + c*c);}
	else{
		st = c;
		sm = sqrt(a*a + b*b);}
	cout << "Nilai Pythagorasnya adalah: " << sm << endl;
	if (sm == st){
		cout << a << ", " << b << ", dan " << c << " merupakan Triple Pythagoras" << endl;}
	else{
		cout << a << ", " << b << ", dan " << c << " bukan Triple Pythagoras" << endl;}
	return 0;
}