int f(int n, int m)
{
    if ((n == m) || (m == 0))
        return 1;
    else
        return f(n - 1, m) + f(n - 1, m - 1);
}
