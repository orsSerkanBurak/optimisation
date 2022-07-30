clc; clear; close all;
syms x
alpha = 0.02;
x1 = ones(1,50);
x1(1,1) = 0;
x2 = ones(1,50);
x2(1,1) = 0;
F = 12*x.^2 - 36*x + 48;
Fprime = diff(F);
FdoublePrime = diff(Fprime);

%Gradient descent
for i=1:1:50
   x1(i+1) = x1(i)-(alpha*subs(Fprime,x1(i)));
end

%Newton-type
for i=1:1:50
   x2(i+1) = x2(i)-((subs(Fprime,x2(i)))/(subs(FdoublePrime,x2(i))));
end

fprintf('Due to Gradient Descent method:\n x1 = %f\n x2 = %f\n F = %f\n',x1(end),4-x1(end),subs(F,x1(end)))
fprintf('Due to Newton type method:\n x1 = %f\n x2 = %f\n F = %f\n',x2(end),4-x2(end),subs(F,x2(end)))

figure(1),clf 
xx=[-50:1:50]';  
for  ii=1:length(xx)
    for  jj=1:length(xx)  
        FF(ii,jj)=  4*xx(ii)^2 + 3*xx(jj)^2 - 5*xx(ii)*xx(jj) + 8*xx(ii);
    end
end
mesh(xx,xx,FF);% 
hold  on;% 

plot3(xx,4-xx, 4*xx.^2 + 3*(4-xx).^2 - 5*xx.*(4-xx) + 8*xx ,"m-","LineWidth",2);%
xlabel("x_1");  ylabel("x_2");  % 
hold  off; 
hh=get(gcf,"children");

hold  on 
plot3(1.50,2.50,21.00,"rs","MarkerSize",20,"MarkerFace","r")
