function llike = f2_sarpanel(parm,y,x,W,detval,T)
% PURPOSE: evaluates log-likelihood -- given ML estimates
%  spatial panel autoregressive model using sparse matrix algorithms
% ---------------------------------------------------
%  USAGE:llike = f2_sar(parm,y,x,W,detval,T)
%  where: parm = vector of maximum likelihood parameters
%                parm(1:k-2,1) = b, parm(k-1,1) = rho, parm(k,1) = sige
%         y    = dependent variable vector (N x 1)
%         x    = explanatory variables matrix (N x k)
%         W    = spatial weight matrix
%     detval   = matrix with [rho log determinant] values
%                computed in sar_panel.m using one of Kelley Pace's routines  
%         T    = number of time points
% ---------------------------------------------------
%  RETURNS: a  scalar equal to minus the log-likelihood
%           function value at the ML parameters
% ---------------------------------------------------

% Updated by J.P. Elhorst summer 2008
% REFERENCES: 
% Elhorst JP (2003) Specification and Estimation of Spatial Panel Data Models,
% International Regional Science Review 26: 244-268.
% Elhorst JP (2009) Spatial Panel Data Models. In Fischer MM, Getis A (Eds.) 
% Handbook of Applied Spatial Analysis, Ch. C.2. Springer: Berlin Heidelberg New York.

N = length(W); 
k = length(parm);
b = parm(1:k-2,1);
rho = parm(k-1,1);
sige = parm(k,1);

gsize = detval(2,1) - detval(1,1);
i1 = find(detval(:,1) <= rho + gsize);
i2 = find(detval(:,1) <= rho - gsize);
i1 = max(i1);
i2 = max(i2);
index = round((i1+i2)/2);
if isempty(index)
index = 1;
end;
detm = detval(index,2);

e=y-x*b;
for t=1:T
    t1=1+(t-1)*N;t2=t*N;
    e(t1:t2,1)=e(t1:t2,1)-rho*W*y(t1:t2,1);
end

epe = e'*e;
tmp2 = 1/(2*sige);
llike = -(N*T/2)*log(2*pi*sige) + T*detm - tmp2*epe;