#include<iostream>
#include<vector>
// #include"C:\Program Files\MySQL\MySQL Server 8.0\include\mysql.h" //library to connect to the mysql database server

using namespace std;
class student

{
protected:
    string name;
    long long mobno;
    float cgpa;
    string branch;
    string userid;
    int password;

public:
    student(){
        name=" ";
        mobno=0;
        cgpa=0;
        branch=" ";
    }
    void login();
    void registeration();
    void update();

};

void student:: registeration(){
    cout<<"\t\t1. Enter the name " ;
    cin>>name;
    cout<<"\t\t2. Enter branch ";
    cin>>branch;
    cout<<"\t\t3. Enter cgpa ";
    cin>>cgpa;
    cout<<"\t\t4. Enter mobile number ";
    cin>>mobno;
    cout<<"Registered successfully "<<endl;
    
}

void student::login(){
    cout<<"\t\t 1. Enter user id ";
    cin>>userid;
    cout<<"\t\t 2. Enter the password ";
    cin>>password;
    cout<<"Logged in successfully"<<endl;
    cout<<"\n";
}
void student:: update(){
    cout<<"\t\t1. Enter updated branch ";
    cin>>branch;
    cout<<"\t\t2. Enter updated cgpa ";
    cin>>cgpa;
    cout<<"Updated successfully "<<endl;
    

}

int main(){
    student s1;
    string str="y";
    while(str=="y"){
        int op;
        cout<<" \t\t1. Enter the registration details "<<endl;
        cout<<" \t\t2. Enter login details "<<endl;
        cout<<"\t\t3. Update details "<<endl;
        cout<<"\t\t4. Exit system "<<endl;
        cout<<"Enter the number choice "<<endl;
        cin>>op;
        switch (op)
        {
        case 1:
            s1.registeration();
            break;
        case 2:
            s1.login();
            break;
        case 3:
            s1.update();
            break;
        case 4:
            exit(0);
            break;
        default:
            cout<<"Invalid choice"<<endl;
            break;
        
    }
    cout<<"Do you want to enter more y/n: ";
    cin>>str;
    
    }
    return 0;
}
