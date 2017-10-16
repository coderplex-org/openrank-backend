from framework.Classes import Testcase


tc1 = Testcase()
tc1.id = "1"
tc1.input = '23\n34'
tc1.timeout = 1

tc2 = Testcase()
tc2.id = "2"
tc2.input = """21 34"""
tc2.timeout = 1

java_source_code_with_input = """
                import java.util.*;
                
                class Solution{
                    public static void main(String... args) {
                        Scanner scan = new Scanner(System.in);
                        int sum = scan.nextInt() + scan.nextInt();
                        System.out.println(sum);
                    }
                }
             """

java_source_code_with_no_input = """
                class Solution{
                    public static void main(String... args) {
                        System.out.println("Hello World");
                    }
                }
             """

java_source_code_with_exception = """
                class Solution{
                    public static void main(String... args) {
                        throw new RuntimeException();
                    }
                }
             """

java_source_code_with_compile_error = """
                class Solution{
                    public static void main(String... args) {
                        int a
                    }
                }
             """

python3_source_code_add_two_numbers = """
# s = input() 
# print(s)
# numbers = s.split()
number1 = input()
number2 = input()
 
sum = int(number1) + int(number2)
print(sum)
"""

python2_source_code_add_two_numbers = """ 
number1 = raw_input()
number2 = raw_input()

sum = int(number1) + int(number2)
print sum
"""

c_source_code_add_two_numbers = """
#include<stdio.h>
 
int main() {
   int a, b, sum;
 
   scanf("%d %d", &a, &b);
 
   sum = a + b;
 
   printf("%d", sum);
 
   return(0);
}
"""


c_source_code_add_two_numbers_compile_error = """
#include<stdio.h>
 
int main() {
   int a, b, sum;
 
   scanf("%d %d", &a, &b);
 
   sum = a  b;
 
   printf("%d", sum);
 
   return(0);
}
"""

cpp_source_code_add_two_numbers = """
#include <iostream>
using namespace std;

int main()
{
    int firstNumber, secondNumber, sumOfTwoNumbers;
    
    cin >> firstNumber >> secondNumber;

    // sum of two numbers in stored in variable sumOfTwoNumbers
    sumOfTwoNumbers = firstNumber + secondNumber;

    // Prints sum 
    cout << sumOfTwoNumbers;     

    return 0;
}"""
