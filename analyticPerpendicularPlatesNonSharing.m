% ----- Analytic Solution -> Aligned Perpendicular Plates with no Shared Edge ----- %

% Function Description:
%   analyticPerpendicularPlatesNonSharing.m returns the analytic solution for the view factor (Fij)
%   between two aligned, perpendicular plates with no shared edge of width X
%   emitter length Y, and receiver height Z

% Function Parameters:
%   [] X : width of the shared edge between the two plates
%   [] Y : length of the emitting plate
%   [] e_o : offset of the emitting plate from the x-axis
%   [] Z : height of receiving plate
%   [] r_o : offset of the receiving plate from the x-axis

% Function Output:
%   [] Fij : view factor between the two plates

function Fij = analyticPerpendicularPlatesNonSharing(X, Y, e_o, Z, r_o )
  Fij = ( (X*(Y+e_o)*analyticPerpendicularPlates( (Y+e_o)/X , (Z+r_o)/X )) + ...
    (X*(e_o)*analyticPerpendicularPlates( (e_o)/X , (r_o)/X )) - ...
    (X*(e_o)*analyticPerpendicularPlates( (e_o)/X , (Z+r_o)/X )) - ...
    (X*(Y+e_o)*analyticPerpendicularPlates( (Y+e_o)/X , (r_o)/X )) ) / (X*Y);
  fprintf('Analytic Result: %.15f\n', Fij)
end