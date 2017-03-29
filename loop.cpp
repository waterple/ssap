#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstring>
#include<string>
#include<ctime>

using namespace std;

int main()
{
	time_t timer;
	tm *t;
	int is_done = 0;
	
	timer = time(NULL);
	t = localtime(&timer);
	if((t->tm_hour > 7) && ((t->tm_hour < 16)||((t->tm_hour==16) && (t->tm_min < 30)))){
		goto python;
	}
	
	while(1){
	
		while(1){ // 8시 5분에 자습 신청 시작 
			timer = time(NULL);
			t = localtime(&timer);
			
			if(t->tm_min == 6){
				is_done = 0;
			}
		
			if(is_done == 0 && (t->tm_hour == 8 && t->tm_min == 1)){
				is_done = 1;
				goto python; 
			}
		}
	
		python:;
		
		ifstream in("info.txt");
		string id, pw;
		int _1, _2, _3;
	
		if(!in.is_open()){
			cout << "No Input.txt!" << endl;
			continue;
		}
		
		in >> id >> pw >> _1 >> _2 >> _3;
		in.close();
	
		char cmd[100];
		sprintf(cmd, "python _FILE_ 2017%s %s %d %d %d", id.c_str(), pw.c_str(), _1, _2, _3);
		is_done = 1;
		system(cmd);
		
	}
	return 0;
}
