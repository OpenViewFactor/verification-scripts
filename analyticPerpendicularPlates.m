% ----- Analytic Solution -> Aligned Perpendicular Plates with a Shared Edge ----- %

% Function Description:
%   analyticPerpendicularPlates.m returns the analytic solution for the view factor (Fij)
%   between two aligned, perpendicular plates with a shared edge of width X
%   emitter length Y, and receiver height Z

% Function Parameters:
%   [] W -> Y/X : Y = length of emitting plate; X = width of the shared edge between the two plates
%   [] H -> Z/X : Z = height of receiving plate

% Function Output:
%   [] Fij : view factor between the two plates

function Fij = analyticPerpendicularPlates(W, H)
  if (W ~= 0 && H ~= 0)
    Fij = (1/(pi * W)) * ( W * atan(1/W) + H * atan(1/H) - sqrt(H^2 + W^2) * atan(1/sqrt(H^2 + W^2)) + ...
      (1/4) * log( ( (1 + W^2)*(1 + H^2) ) / (1 + W^2 + H^2) * ...
      ( (W^2 * (1 + W^2 + H^2)) / ( (1 + W^2)*(W^2 + H^2) ) )^(W^2) * ...
      ( (H^2 * (1 + W^2 + H^2)) / ( (1 + H^2)*(W^2 + H^2) ) )^(H^2) ) );
  else
    Fij = 0;
  end
  fprintf('Analytic Result: %.15f\n', Fij)
end