
int fibonacciSequence(int n) {
    if (n == 0 || n == 1) {
        return n;
    } else {
        return fibonacciSequence(n-1) + fibonacciSequence (n-2);
    }
}
