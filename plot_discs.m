clear all
close all
clc

set(groot, "defaultAxesTickLabelInterpreter", "latex")
set(groot, "defaulttextInterpreter", "latex")
set(groot, "defaultLegendInterpreter","latex")

output_path = "test_outputs/pdfs/";
paper_size = 12;


%! -- PARALLEL DISCS (r=1)
%! DISTMESH GENERATION


dai_numeric = [ 0.382117982635409, 0.381959483020725, 0.381963830337079, 0.381964944808842, 0.381963830337078, 0.381964944808842 ];
sai_numeric = [ 0.376121107621998, 0.38054762080434, 0.381795640715257, 0.381886716661892, 0.381957769357435, 0.381962598085556 ];



analytic = 0.381966011250105;


N = [ 400, 22801, 442225, 7817616, 317801929, 2114344324 ];

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);


dai_vf_time = [ 0.0075901, 0.0050979, 0.0093944, 0.0805209, 1.93455, 14.8848 ];
dai_runtime = dai_vf_time;

sai_vf_time = [ 0.0058043, 0.0079022, 0.016179, 0.100047, 2.75756, 18.3439 ];
sai_runtime = sai_vf_time;


figure(1)
loglog(N, dai_errors, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_errors, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Absolute Error")
legend("DAI","SAI")
xlim([1e2,1e10])
xticks([1e2,1e3,1e4,1e5,1e6,1e7,1e8,1e9,1e10])
set(gca,"XTickLabelRotation",0)
ylim([1e-7,1e-2])
yticks([1e-7,1e-6,1e-5,1e-4,1e-3,1e-2])
set(gca, "FontSize", 18)
set(figure(1),'Units','centimeters')
set(figure(1),'PaperUnits','centimeters')
set(figure(1),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "par-discs-r=1-convergence.pdf";
pause(1.5)
exportgraphics(figure(1), full_file_name)
hold off

figure(2)
loglog(N, dai_runtime, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_runtime, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Runtime [s]")
legend("DAI","SAI", "Location", "northwest")
xlim([1e2,1e10])
xticks([1e2,1e3,1e4,1e5,1e6,1e7,1e8,1e9,1e10])
set(gca,"XTickLabelRotation",0)
ylim([1e-3,1e2])
yticks([1e-3,1e-2,1e-1,1e0,1e1,1e2])
set(gca, "FontSize", 18)
set(figure(2),'Units','centimeters')
set(figure(2),'PaperUnits','centimeters')
set(figure(2),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "par-discs-r=1-runtime.pdf";
pause(1.5)
exportgraphics(figure(2), full_file_name)
hold off





%! -- PARALLEL DISCS (r=1)
%! NEW MESH GENERATION

analytic = 0.381966011250105;

dai_numeric = [ 0.37951784268582 , 0.381388558835403 , 0.381834879875496 , 0.381935428062461 , 0.38195882542184 ];
sai_numeric = [ 0.378518794862217 , 0.381126735080451 , 0.381763135994406 , 0.381916412097671 , 0.381953842335203 ];
N = [ 21316 , 232324 , 2722500 , 37576900 , 542051524 ];

dai_vf_time = [ 0.0091411 , 0.0098015 , 0.0314775 , 0.284287 , 3.50359 ];
sai_vf_time = [ 0.0065928 , 0.0127482 , 0.044214 , 0.363938 , 4.65276 ];

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);

dai_runtime = dai_vf_time;
sai_runtime = sai_vf_time;


figure(3)
loglog(N, dai_errors, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_errors, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Absolute Error")
legend("DAI","SAI")
xlim([1e4,1e9])
xticks([1e4,1e5,1e6,1e7,1e8,1e9])
set(gca,"XTickLabelRotation",0)
ylim([1e-6,1e-2])
yticks([1e-6,1e-5,1e-4,1e-3,1e-2])
set(gca, "FontSize", 18)
set(figure(3),'Units','centimeters')
set(figure(3),'PaperUnits','centimeters')
set(figure(3),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "par-discs-r=1-convergence-new-circles.pdf";
pause(1.5)
exportgraphics(figure(3), full_file_name)
hold off




figure(4)
loglog(N, dai_runtime, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_runtime, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Runtime [s]")
legend("DAI","SAI", "Location", "northwest")
xlim([1e4,1e9])
xticks([1e4,1e5,1e6,1e7,1e8,1e9])
set(gca,"XTickLabelRotation",0)
ylim([1e-3,1e1])
yticks([1e-3,1e-2,1e-1,1e0,1e1])
set(gca, "FontSize", 18)
set(figure(4),'Units','centimeters')
set(figure(4),'PaperUnits','centimeters')
set(figure(4),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "par-discs-r=1-runtime-new-circles.pdf";
pause(1.5)
exportgraphics(figure(4), full_file_name)
hold off