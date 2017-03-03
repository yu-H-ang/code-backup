% clear memory and screen
clear;clc;

% parameters
L = 1;
U0 = 1;
Lambda = 100;
v = 1;
N = 30;
X = 0:L/(N-1):L;

% exact solutions
u1 = @(x) U0*sinh(sqrt(Lambda)*(L-x))/sinh(sqrt(Lambda)*L);
u2 = @(x) -(v/sqrt(Lambda))*sinh(sqrt(Lambda)*(L-x))/cosh(sqrt(Lambda)*L);
U1 = u1(X);
U2 = u2(X);

% build the systems and solve
x1 = Helmholtz_tridiagonal_solve(Lambda, L, U0, N, 1, v);
x2 = Helmholtz_tridiagonal_solve(Lambda, L, U0, N, 2, v);

% plot the results
figure;plot(X, x1);hold on;plot(X, U1,'.r');legend('numerical','exact');
figure;plot(X, x2);hold on;plot(X, U2,'.r');legend('numerical','exact');

function x = Helmholtz_tridiagonal_solve(Lambda, L, U0, N, numBC, v)
% matrix initialization
dx = L / (N - 1);
e = ones(N, 1);
f = -(2 + dx^2 * Lambda) * ones(N, 1);
g = ones(N, 1);
r = zeros(N, 1);
% boundary condition
if numBC == 1
    % BC1
    f(1) = 1;g(1) = 0;r(1) = U0;
    f(N) = 1;e(N) = 0;r(N) = 0;
elseif numBC == 2
    % BC2, use ghost cell
    g(1) = 2;r(1) = 2*dx*v;
    f(N) = 1;e(N) = 0;r(N) = 0;
else
    msg = 'Error occurred: boundary condition number must be 1 or 2.';
    error(msg);
end
% tridiagonal solve
x = Tridiag(e, f, g, r);
end

% from the book
function x = Tridiag(e, f, g, r)
% Tridiag: Tridiagonal equation solver banded system
% x = Tridiag(e,f,g,r): Tridiagonal system solver.
% input:
% e = subdiagonal vector
% f = diagonal vector
% g = superdiagonal vector
% r = right hand side vector
% output:
% x = solution vector
n = length(f);
% forward elimination
for k = 2:n
    factor = e(k)/f(k-1);
    f(k) = f(k) - factor*g(k-1);
    r(k) = r(k) - factor*r(k-1);
end
% back substitution
x(n) = r(n)/f(n);
for k = n-1:-1:1
    x(k) = (r(k)-g(k)*x(k+1))/f(k);
end
end
