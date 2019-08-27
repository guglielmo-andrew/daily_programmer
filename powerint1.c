#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct Ans {
    int number;
    struct Ans *next;
};

void printList(struct Ans *n);

void main (void) { 

    int x = 2;
    int y = 3;
    int bound = 10;

    struct Ans *answer_ptr = malloc(sizeof(struct Ans));
    struct Ans *start_ptr = answer_ptr;

    for (int a = 0; a <= bound; a++)
    {
        for (int i = 0; i < bound; i++) {
            for (int j = 0; j < bound; j++) {
                if (pow(x,i) + pow(y,j) == a) {
                    answer_ptr->number = a;
                    answer_ptr->next = malloc(sizeof(struct Ans));
                    answer_ptr = answer_ptr->next;
                }
            }
        }
    }
    printf("Answers: ");
    printList(start_ptr);
    printf("\n");
};

void printList(struct Ans *n) 
    { 
        while (n->next != NULL) { 
            printf(" %i ", n->number); 
            n = n->next; 
        } 
    };