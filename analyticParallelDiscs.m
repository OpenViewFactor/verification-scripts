% ----- Analytic Solution -> Aligned Parallel Discs ----- %

% Function Description:
%   parallel_discs.m returns the analytic solution for the view factor (Fij)
%   between two aligned, parallel discs with radii ri and rj, separated by
%   distance L

% Function Parameters:
%   [] ri = radius of the emitting disc
%   [] rj = radius of the receiving disc
%   [] L = distance between the two discs

% Function Output:
%   [] Fij : view factor between the two plates

function Fij = analyticParallelDiscs(ri, rj, L)
  Ri = ri/L;
  Rj = rj/L;
  S = 1 + ( (1+Rj^2)/ Ri^2);
  Fij = (1/2) * ( S - sqrt( S^2 - 4*( rj/ri )^2 ) );

  fprintf('Analytic Result: %.15f\n', Fij)
end