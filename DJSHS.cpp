#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstring>
#include<string>

using namespace std;

int main()
{	
	ifstream in("info.txt");
	string id;
	string pw;
	int _1, _2, _3;
	
	in >> id >> pw >> _1 >> _2 >> _3;
	
	if(!in.is_open()){
		cout << "No Input.txt!" << endl;
		return 0;
	}
	
	char cmd[100];
	sprintf(cmd, "python _FILE_ 2017%s %s %d %d %d", id.c_str(), pw.c_str(), _1, _2, _3);
	
	system(cmd);
	return 0;
}
