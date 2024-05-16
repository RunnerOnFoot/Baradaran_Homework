int f(char *e)
{
    struct Stack *s;
    s = create(strlen(e));
    for (i = 0; e[i]; ++i)
    {
        if (isdigit(e[i]))
            push(s, e[i] - '0');
        else
        {
            a = pop(s);
            b = pop(s);
            switch (e[i])
            {
            case '+':
                push(s, b + a);
                break;
            case '-':
                push(s, b - a);
                break;
            case '*':
                push(s, b * a);
                break;
            case '/':
                push(s, b / a);
                break;
            }
        }
    }
    return pop(s);
}