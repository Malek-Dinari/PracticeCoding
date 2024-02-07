#include <iostream>

using namespace std;

int main()
{

    // BMI Calculator
    // weight(kg) / height(m)
    // underweight: <18.5
    // normal weight: in [18.5, 25]
    // overweight:  >25

    float weight, height;

    cout << "Weight(kg), height(m): ";
    cin >> weight >> height;
    float bmi = weight / (height * height);

    if (bmi < 18.5)
        cout << "Underweight" << endl;

    else if (bmi > 25)
        cout << "Overweight" << endl;

    else
        cout << "Normal weight";

    cout << "Your BMI is: " << bmi;

    system("pause>0");
    return 1;
}