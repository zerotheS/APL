#include <iostream>
#include <conio.h>
#include <stdio.h>
using namespace std;

string str[5], temp;

void input() {
    for(int i=0;i<5;i++) {
        cout<<"Masukkan kalimat ke-"<<(i+1)<<" = ";
        getline(cin, str[i]);
        }
    cout<<endl;
    }

void tampil() {
    for(int i=0;i<5;i++) {
        cout<<str[i]<<", ";
        }
    cout<<endl;
    }

void exchange_sort_ascending() {
    for (int i=0; i<5-1; i++) {
        for(int j = (i+1); j<5; j++) {
            if(str[i]>str[j]){
                temp = str[i];
                str[i] = str[j];
                str[j]=temp;
                }
            }
        tampil();
        }
    cout<<endl;
    }

void exchange_sort_descending() {
    for (int i=0; i<5-1; i++) {
        for(int j = (i+1); j<5; j++) {
            if(str[i]<str[j]){
                temp = str[i];
                str[i] = str[j];
                str[j]=temp;
            }
            }
        tampil();
        }
    cout<<endl;
    }

void pilihan() {
    int pil;
    cout << "1. Ascending | 2. Descending" << endl;
    cout << "Masukkan pilihan sorting : "; cin >> pil; cout << endl;
    if (pil==1)
    cout << "Sorting berdasarkan Ascending:" << endl,
    cout << "------------------------------" << endl,
    tampil(), exchange_sort_ascending();
    else if(pil==2)
    cout << "Sorting berdasarkan Descending:" << endl,
    cout << "-------------------------------" << endl,
    tampil(), exchange_sort_descending();
    else
    cout << "Input yang anda masukkan tidak valid." << endl;
    }

void utama() {
system("cls");
    cout << "============================" << endl;
    cout << "||                        ||" << endl;
    cout << "||      Exchange Sort     ||" << endl;
    cout << "||     Kelompok 24 APL    ||" << endl;
    cout << "||                        ||" << endl;
    cout << "============================\n" << endl;
input();
    cout << "====Proses Exchange Sort====" << endl;
    cout << "----------------------------" << endl;
pilihan();
    }

main() {
utama();
    cout << "Tekan Enter untuk keluar...";
getch();
    }