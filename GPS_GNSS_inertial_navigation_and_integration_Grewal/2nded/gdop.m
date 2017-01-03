% gdop.m
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Calculate GDOP and store in output variable array for plotting %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

A           = inv(H(1:4,1:4)'*H(1:4,1:4));
gdop_out(k) = sqrt(trace(A));