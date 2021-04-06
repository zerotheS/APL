#include <iostream>
using namespace std;

int main() {
    int angka[2][3]={{3,1,4},{2,8,5}};
    int i, j, data[i];
    float sum = 0, max = 0, min = 6, a = 6;
    cout << "\nMatriks :" << endl;
    for(i=0; i<2; i++) {
        for(j=0; j<3; j++)
        cout << angka[i][j]<<" ";
        cout << endl;
        }
    cout << "\nData matriks adalah ";
    for(i=0; i<6; i++) {
        cout << data[i] << ',';
        sum = sum + data[i];
    if (max < data[i]) {
        max = data[i];
        }
    if (min > data[i]) {
        min = data[i];
        }
    }
    cout << "\nJumlah data : " << sum;
    cout << "\nNilai rata-rata : " << sum/a;
    cout << "\nBilangan terkecil :" << min;
    cout << "\nBilangan terbesar : " << max;
    cout << "\n\n================================\n";
}