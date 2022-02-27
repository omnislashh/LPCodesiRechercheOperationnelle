/* https://martin-thoma.com/how-to-use-glpk/#assignment-problem */
param m, integer, > 0;
/* number of suppliers */

param n, integer, > 0;
/* number of clients */

set I := 1..m;
/* set of suppliers */

set J := 1..n;
/* set of clients */

param c{i in I, j in J}, >= 0;
/* cost of allocating task j to supplier i */

var x{i in I, j in J}, >= 0;
/* x[i,j] = 1 means task j is assigned to supplier i
   note that variables x[i,j] are binary, however, there is no need to
   declare them so due to the totally unimodular constraint matrix */

s.t. phi{i in I}: sum{j in J} x[i,j] <= 8;
/* each supplier can perform at most one task */

s.t. psi{j in J}: sum{i in I} x[i,j] = 1;
/* each task must be assigned exactly to one supplier */

minimize obj: sum{i in I, j in J} c[i,j] * x[i,j];
/* the objective is to find a cheapest assignment */

solve;

printf "\n";
printf "supplier  Task       Cost\n";
printf{i in I} "%5d %5d %10g\n", i, sum{j in J} j * x[i,j],
   sum{j in J} c[i,j] * x[i,j];
printf "----------------------\n";
printf "     Total: %10g\n", sum{i in I, j in J} c[i,j] * x[i,j];
printf "\n";

data;

param m := 4;

param n := 8;

param c : 1  2  3  4  5  6  7  8 :=
      1   5  3  4  7 10 10  5  3
      2   2  0  1  4  7 13  8  6
      3  10  8 10 13 10  5  0  2
      4  11  9  7  4  2  3  8 11 ;

end;
