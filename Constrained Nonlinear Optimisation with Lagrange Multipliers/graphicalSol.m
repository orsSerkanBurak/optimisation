clear;clc; close all;
figure(1),clf 
xx=[-500:10:500]';  
for  ii=1:length(xx)
    for  jj=1:length(xx)  
        FF(ii,jj)=  xx(ii)^2+320*xx(ii)*xx(jj);
    end
end
hh=mesh(xx,xx,FF);% 
hold  on;% 

plot3(xx,xx/60,xx.^2+(320/60)*xx.^2,"m-","LineWidth",2);  %first constraint
plot3(xx,xx-(3600./xx),xx.^2+320.*xx.*(xx-(3600./xx)),"g-","LineWidth",2); %second constraint

xlabel("x_1");  ylabel("x_2");  % 
hold  off;  %axis([-3  3  -3  3  0  20])% 
hh=get(gcf,"children");% 
%set(hh,"View",[-109  74],"CameraPosition",[-26.5555  13.5307  151.881]);% 

xx=fmincon("exampleF",[0;0],[],[],[],[],[],[],"exampleC"); 
hold  on 
plot3(xx(1),xx(2),xx(1)^2+320*xx(1)*xx(2),"rs","MarkerSize",20,"MarkerFace","r") 
xx(1)^2+320*xx(1)*xx(2) 

%[x,fval,exitflag,output,lambda,grad,hessian] = fmincon("exampleF",[0;0],[],[],[],[],[],[],"exampleC");

function  [c,ceq]=exampleC(X)
    c1 = (1/100)*(X(1)-(60*X(2))); 
    c2 = 1-(X(1)*(1/3600)*(X(1)-X(2)));
    c3 = -X(1);
    c4 = -X(2);
    c=[c1;c2;c3;c4]; 
    ceq=0; 
return 
end

function  F = exampleF(X) 
    F=X(1)^2+320*X(1)*X(2); 
return 
end