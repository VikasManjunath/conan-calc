#include <iostream>
#include "calculator.h"

using namespace std;

Calculator::Calculator(/* args */)
{
    cout<< "Calculator initialized";
}

Calculator::~Calculator()
{
}

int Calculator::sum(int a, int b){
    return a+b;
}
