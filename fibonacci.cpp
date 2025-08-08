#include <iostream>
#include <vector>
using namespace std;

// Method 1: Iterative approach (most efficient)
void fibonacciIterative(int n) {
    cout << "Fibonacci series (first " << n << " numbers) - Iterative:" << endl;
    
    if (n <= 0) return;
    
    long long first = 0, second = 1;
    
    if (n >= 1) cout << first << " ";
    if (n >= 2) cout << second << " ";
    
    for (int i = 3; i <= n; i++) {
        long long next = first + second;
        cout << next << " ";
        first = second;
        second = next;
    }
    cout << endl;
}

// Method 2: Recursive approach (simple but inefficient for large n)
long long fibonacciRecursive(int n) {
    if (n <= 1) return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

void printFibonacciRecursive(int n) {
    cout << "Fibonacci series (first " << n << " numbers) - Recursive:" << endl;
    for (int i = 0; i < n; i++) {
        cout << fibonacciRecursive(i) << " ";
    }
    cout << endl;
}

// Method 3: Dynamic Programming approach (memoization)
void fibonacciDP(int n) {
    cout << "Fibonacci series (first " << n << " numbers) - Dynamic Programming:" << endl;
    
    if (n <= 0) return;
    
    vector<long long> fib(n);
    
    if (n >= 1) fib[0] = 0;
    if (n >= 2) fib[1] = 1;
    
    for (int i = 2; i < n; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }
    
    for (int i = 0; i < n; i++) {
        cout << fib[i] << " ";
    }
    cout << endl;
}

int main() {
    int n;
    
    cout << "Enter the number of Fibonacci numbers to print: ";
    cin >> n;
    
    cout << endl;
    
    // Using iterative method (recommended for large numbers)
    fibonacciIterative(n);
    
    cout << endl;
    
    // Using recursive method (only for small numbers due to exponential time complexity)
    if (n <= 20) {
        printFibonacciRecursive(n);
        cout << endl;
    } else {
        cout << "Skipping recursive method for n > 20 (too slow)" << endl << endl;
    }
    
    // Using dynamic programming method
    fibonacciDP(n);
    
    return 0;
}