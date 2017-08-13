//******************************************************************
// Template Program
// Programmer: Alan Ngo
// Completed : November 12 2016
// Status    : Complete
//
// This program will be used...
//******************************************************************
/* PROMPT*/
#include <iostream>				// for cin, cout, endl
#include <cmath>
#include <iomanip>
#include <fstream>
#include <string>
#include <iomanip>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int main()						
{ 
 //m-km
 double miles=0;
 double kilometers=0;
 cout<<"Enter the number of miles you want to convert ";
 cin>>miles;
 kilometers=1.6*miles;
 cout<<miles<<" miles = "<<kilometers<<" kilometers"<<endl;
 //f-c
 double farenheit=0;
 double celcius=0;
 cout<<"Enter the number of farenheit you want to convert ";
 cin>>farenheit;
 celcius=5*(farenheit - 32)/9;
 cout<<farenheit<<" farenheit = "<<celcius<<" celcius"<<endl;
 //g-L
 double gallons=0;
 double liters=0;
 cout<<"Enter the number of gallons you want to convert ";
 cin>>gallons;
 liters=3.9*gallons;
 cout<<gallons<<" gallons = "<<liters<<" liters"<<endl;
 //lb-kg
 double pounds=0;
 double kilograms=0;
 cout<<"Enter the number of pounds you want to convert ";
 cin>>pounds;
 kilograms=.45*pounds;
 cout<<pounds<<" pounds = "<<kilograms<<" kilograms"<<endl;	
 //in-cm
 double inches=0;
 double centimeters=0;
 cout<<"Enter the number of inches you want to convert ";
 cin>>inches;
 centimeters=2.54*inches;
 cout<<inches<<" inches = "<<centimeters<<" centimeters"<<endl;
 return 0;
}   // end of main function
