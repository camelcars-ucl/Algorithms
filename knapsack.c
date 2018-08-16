#include <stdio.h>

/*
This is the 0-1 knapsack problem solved using dynamic programming
*/
// I stands for index, which should be the length of w + 1
// SIZE stands for the knapsack size
#define I 6
#define SIZE 20

int max(int a, int b);
int knapsack(int p[], int w[]);

int main()
{
  int p[] = {7, 3, 8, 6, 5};
  int w[] = {10, 15, 2, 4, 5};
  int ans = knapsack(p, w);
  printf("%d\n", ans);
}
int knapsack(int p[], int w[]){
  int k[I][SIZE+1];
  for (int i = 0; i < SIZE+1; ++i)
  {
    k[0][i] = 0;
  }
  for (int i = 1; i < I; ++i){
    for (int s = 0; s < SIZE+1; ++s)
    {
      if (w[i-1] > s) k[i][s] = k[i-1][s];
      else k[i][s] = max(p[i-1] + k[i-1][s-w[i-1]], k[i-1][s]);
    }
  }
  return k[I-1][SIZE];
}

int max(int a, int b){
  if (a>b) return a;
  else return b;
}