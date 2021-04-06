#include <iostream>

using namespace std;

int main(){

     // Deklarasi array multidimensi dengan nama "angka"
     // Dengan jumlah ukuran pertama / subskrip pertama = 1
     // Jumlah Ukuran kedua = 2 & jumlah ukuran ketiga = 3
     int angka [1][2][3];

     // Mendeklarasi variabel untuk indeks perulangan
     int i,j,k,n=6,total=0;
     float rata;

     cout<<"\t===============================";
     cout<<"\n\t== Array Multidimensi ==\n";
     cout<<"\t===============================\n\n";

     // Mengisi nilai kedalam elemen-elemen array angka
     cout<<"== Masukkan elemen-elemen array angka ==\n";
     for(i=0;i<1;i++){
          for(j=0;j<2;j++){
               for(k=0;k<3;k++){
                    cout<<"angka indeks ke ["<<i<<"]["<<j<<"]["<<k<<"]"<<" = ";
                    cin>>angka[i][j][k];
               }
          }
     }

     cout<<"\n\n===============================\n";
     cout<<"== Tampil nilai elemen Array ==\n";
     cout<<"===============================\n";

     //menampilkan nilai dari setiap elemen array angka
     for(i=0;i<1;i++){
          for(j=0;j<2;j++){
               for(k=0;k<3;k++){
               cout<<"angka indeks ke ["<<i<<"]["<<j<<"]["<<k<<"]"<<" = "<<angka[i][j][k]<<endl;
          }
     }
}

     cout<<"\n\n===============================\n";
     cout<<"== Nilai rata-rata elemen Array ==\n";
     cout<<"===============================\n";

	//menampilkan nilai rata-rata elemen
	for(i=0;i<1;i++)
          for(j=0;j<2;j++)
               for(k=0;k<3;k++)
               total = total + angka[i][j][k];
			rata = total/n;
          cout << "Total nilai adalah = " <<total << endl;
          cout << "Hasil rata-rata adalah = " << rata << endl;

	return 0;
}