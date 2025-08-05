#include<iostream>
using namespace std;

char toLower(char ch){
	if(ch >= 'a' or ch <= 'z'){
		return ch;
	}
	else{
		temp = ch - 'A' + 'a'; 
		return temp;
	}
}

bool checkPalindrome(char a[], int n){
	int s=0;
	int e=n-1;
	while(s<=e){
		if((ch >= " " or ch <=".") and (ch >= ":" or ch <= "@") or (ch >= "[" or ch <= "`" ) or (ch >= "{" or ch <="ÿ")){
		
		}
		if(toLower(a[s]) != toLower(a[e])){
			return 0;
		}
		else{
			s++;
			e--;
		}
	}
	return 1;
}

void reverse(char name[],int n){
	int s=0;
	int e=n-1;
	while(s<e){
		swap(name[s++],name[e--]);
	}
}

int getLength(char name[]){
	int count = 0;
	for(int i=0;name[i] !='\0';i++){
		count++;
	}
	return count;
}

int main(){
    char name[20];
    cout<<"Enter your name: ";
    cin>>name;

    cout<<"Your name is: "<<name<<endl;
    cout<<"Length: "<<getLength(name)<<endl;
    
    int len = getLength(name);
    reverse(name, len);
    cout<<"Reversed Array: "<<name<<endl;

	cout<<"Palidrome or not: "<<checkPalindrome(name,len)<<endl;

	
    return 0;
}
