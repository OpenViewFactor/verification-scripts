% ----- Analytic Solution -> Aligned Parallel Plates ----- %

% Function Description:
%   parallel_plates.m returns the analytic solution for the view factor (Fij)
%   between two aligned, parallel plates of width X and depth Y

% Function Parameters:
%   [] x_bar -> X/Z : X = width of both plates; Z = distance between the plates
%   [] y_bar -> Y/Z : Y = length of both plates

% Function Output:
%   [] Fij : view factor between the two plates

function Fij = analyticParallelPlates(x_bar, y_bar)
  Fij = ( 2 / (pi * x_bar * y_bar) ) *...
    (  log( sqrt( ( (1 + x_bar^2) * (1 + y_bar^2) ) / ( 1 + x_bar^2 + y_bar^2 ) ) ) +...
    ( x_bar * sqrt( 1+y_bar^2 ) * atan( x_bar / sqrt( 1+y_bar^2 ) ) ) +...
    ( y_bar * sqrt( 1+x_bar^2 ) * atan( y_bar / sqrt( 1+x_bar^2 ) ) ) -...
    ( x_bar * atan(x_bar) ) -...
    ( y_bar * atan(y_bar) ) );

  fprintf('Analytic Result: %.15f\n', Fij)
end