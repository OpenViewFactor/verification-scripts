% ----- Analytic Solution -> Concentric Cylinders ----- %

% Function Description:
%   concentric_cylinders.m returns the analytic solution for the set of view factors (Fij)
%   between two coaxial cylinders with radii ri and ro of height H
%   IMPORTANT: inner cylinder is assumed to have a view radially outwards
%   IMPORTANT: outer cylinder is assumed to have a view radially inwards

% Function Parameters:
%   [] ri = radius of the inner cylinder
%   [] ro = radius of the outer cylinder
%   [] H = height of the two cylinders

% Function Output:
%   [] F12 : view factor from inner -> outer
%   [] F13 : view factor from inner -> surroundings
%   [] F21 : view factor from outer -> inner
%   [] F22 : view factor from outer -> outer
%   [] F23 : view factor from outer -> surroundings

function [F12, F13, F21, F22, F23] = analyticConcentricCylinders(ri, ro, H)
  a1 = 2*pi*ri * H;
  a2 = 2*pi*ro * H;

  h = H/ri;
  R = ro/ri;

  f1 = h^2 + R^2 - 1;
  f2 = h^2 - R^2 + 1;
  f3 = sqrt((f1+2)^2 - 4*R^2);
  f4 = f3 * acos(f2/(R*f1)) + f2 * asin(1/R) - (pi*f1)/2;
  f5 = sqrt(((4*R^2)/h^2) + 1);
  f6 = 1 - ((2*h^2) / (R^2*(h^2+4*R^2-4)));
  f7 = f5 * asin(f6) - asin(1 - 1/R^2) + (pi/2 * (f5-1));

  F12 = 1 - ((1/pi)*(acos(f2/f1) - f4/(2*h)));
  F21 = F12 * a1/a2;
  F13 = 1 - F12;
  F22 = 1 - (1/R) + ((2/(pi*R)) * atan(2*sqrt(R^2-1)/h)) - (h*f7)/(2*pi*R);
  F23 = 1 - F21 - F22;

  fprintf('Analytic Result: %.15f\n', F12)
end