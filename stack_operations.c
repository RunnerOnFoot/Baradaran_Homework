#include <stdio.h>
#include <conio.h>

struct stack
{
    int a[10];
    int top;
};

void create(struct stack *s)
{
    s->top = -1;
}

int isfull(struct stack *s)
{
    if (s->top == 9)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isempty(struct stack *s)
{
    if (s->top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void push(struct stack *s)
{
    int x;
    printf("Enter: ");
    scanf("%d", &x);
    if (isfull(s))
    {
        printf("Stack is full");
    }
    else
    {
        s->top++;
        s->a[s->top] = x;
    }
}

void pop(struct stack *s)
{
    if (isempty(s))
    {
        printf("\nStack is empty\n");
    }
    else
    {
        printf("pop= %d", s->a[s->top]);
        s->top--;
    }
}

main()
{
    struct stack *x;
    int a = 1;
    create(x);
    push(x);
    push(x);
    push(x);
    pop(x);
}