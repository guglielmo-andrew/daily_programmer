#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

struct Ans {
    int number;
    struct Ans *next;
};

//Prototypes
void printList(struct Ans *n);
bool inList(struct Ans *m, int x);

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
                // See if x^i + y^j = a number
                if (pow(x,i) + pow(y,j) == a) {
                    // If true, see if number is already in thie list
                    if (!inList(start_ptr, a)) {
                        // If not, put the number in the list and create new link
                        answer_ptr->number = a;
                        answer_ptr->next = malloc(sizeof(struct Ans));
                        answer_ptr = answer_ptr->next;
                    }
                }
            }
        }
    }
    // Print out answers
    printf("Answers: ");
    printList(start_ptr);
    printf("\n");
};

// A function to print the linked list
void printList(struct Ans *n) { 
    while (n->next != NULL) { 
        printf(" %i ", n->number); 
        n = n->next; 
    } 
};

// A function to see if a number is in the linked list already
bool inList(struct Ans *m, int x) {
    while (m->next != NULL) {
        if (m->number == x) {
            return true;
        }
        m = m-> next;
    }
    return false;
};