clear; clc; close all;
syms x1 x2 lambda1 lambda2 lambda3 lambda4
%case 1: all multipliers are inactive
fprintf('Case 1: All multipliers are inactive\n');
f1 = 2*x1 +  320*x2 == 0;
f2 = 320*x2 == 0;
solve(f1,f2)

%case 2: lambda1 is active and lambda2, lambda3 and lambda4 are inactive
fprintf('\nCase 2: lambda1 is active and lambda2, lambda3 and lambda4 are inactive\n');
f3 = 2*x1 + 320*x2 + lambda1/100 == 0;
f4 = 320*x1 - ((3*lambda1)/5) == 0;
f5 = lambda1*((x1-(60*x2))/100) == 0;
solve(f3,f4,f5)

%case 3: lambda2 is active and lambda1, lambda3 and lambda4 are inactive
fprintf('\nCase 3: lambda2 is active and lambda1, lambda3 and lambda4 are inactive\n');
f6 = 2*x1 + 320*x2 + lambda2*((x1/1800)-(x2/3600)) == 0;
f7 = 320*x1 - ((lambda2*x1)/3600) == 0;
f8 = lambda2*(1-((x1/3600)*(x1-x2))) == 0;
solve(f6,f7,f8)

%case 4: lambda1 and lambda2 are active and lambda3 and lambda4 are
%inactive
fprintf('\nCase 4: lambda1 and lambda2 are active and lambda3 and lambda4 are inactive\n');
fA = 2*x1 + 320*x2 + lambda1/100 - lambda2*(x1/1800 - x2/3600) == 0;
fB = 320*x1 - (3*lambda1)/5 + (lambda2*x1)/3600 == 0;
fC = lambda1*(x1/100 - (3*x2)/5) == 0;
fD = lambda2*(1 - (x1*(x1 - x2))/3600) == 0;
[lambda1,lambda2,x1,x2] = solve(fA,fB,fC,fD);
x1 = double(x1)
x2 = double(x2)
lambda1 = double(lambda1)
lambda2 = double(lambda2)

%for i = 1:1:3
%    if (x1(i) > 0) & (x2(i)>0) & (((x1(i)-(60*x2(i)))/100) < 0) & ((1-((x1(i)*(x1(i)-x2(i)))/3600)) < 0)
%        xx1 = x1(i);
%        xx2 = x2(i);
%    end
%end

fprintf('\nWith results which satisfy the constraints, minimum of the function is:\n');
F = x1(3)^2 + 320*x1(3)*x2(3)