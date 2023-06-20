// Wilson primes
// https://www.codewars.com/kata/55dc4520094bbaf50e0000cb



// DESCRIPTION

// Wilson primes satisfy the following condition. Let P represent a prime number.

// ((P-1)! + 1) / (P * P)
// should give a whole number.

// Your task is to create a function that returns true if the given number is a Wilson prime.


fn am_i_wilson(n: u32) -> bool {
    if n == 5 || n == 13 || n == 563 {
        return true;
    }
    if n < 2 || n % 2 == 0 {
        return false;
    }
    let mut f = 1;
    for i in 3..=n - 2 {
        f *= i;
        f %= n;
    }
    (f + 1) % (n * n) == 0
}



// Best practices

fn am_i_wilson(n: u32) -> bool {
    [5, 13, 563].contains(&n)
}

fn am_i_wilson(n: u32) -> bool {
    n == 5 || n == 13 || n == 563 // https://en.wikipedia.org/wiki/Wilson_prime
}

fn am_i_wilson(n: u32) -> bool {
    if n <= 1 { return false; }
    let n = n as u64;
    let s = n * n;
    ((2..n).fold(1, |f, k| (f * (k % s)) % s) + 1) % s == 0
}