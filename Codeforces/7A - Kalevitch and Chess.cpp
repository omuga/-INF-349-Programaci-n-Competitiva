#include <iostream>
#include <vector>
#include <string.h>
#include <bitset>         // std::bitset
using namespace std;


int main() {

  string linea;
  vector<string> tablero;
  int cols_black = 0;
  int rows_black = 0;
  int final;
  bool cols_check = false;
  for (int i = 0; i  < 8; i++){
  		cin >> linea;
  		if (linea.compare("BBBBBBBB") == 0){
  			rows_black += 1;
  		} else 
  			{
  			if (!cols_check){
	  			for (int a = 0; a < linea.size(); a ++)
	  			{
	  				if (linea[a] == 'B'){
	  					cols_black += 1;
	  				}
	  			}
	  		}
	  		cols_check = true;
  			}
  		}
  final = rows_black + cols_black;
  cout << final;
  return 0;
} 