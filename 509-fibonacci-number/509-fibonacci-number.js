/**
 * @param {number} n
 * @return {number}
 */
var fib = (n, memo = {} )=>{
    if (n==1) return 1;
    else if (n==0 )return 0;
    else{
        if (n in memo){
            return memo[n];
        }
        memo[n]=fib(n-1, memo)+fib(n-2, memo);
    }
    return memo[n];
}