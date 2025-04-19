clear all
close all
clc

set(groot, "defaultAxesTickLabelInterpreter", "latex")
set(groot, "defaulttextInterpreter", "latex")
set(groot, "defaultLegendInterpreter","latex")

output_path = "test_outputs/pdfs/";
paper_size = 12;

%!-- CYLINDERS (r=0.125 -> r=0.25)

dai_numeric = [ 0.917101052188805, 0.912731004800055, 0.911640037756579, 0.911203300349212, 0.910986846300265, 0.910929363145809 ];
sai_numeric = [ 0.909216940224427, 0.910346953734093, 0.910657876217912, 0.910776070185348, 0.910836207749596, 0.910851807137809 ];
analytic = 0.910868433007748;

bfcull_time = [ 0.0120999, 0.0321645, 0.143015, 0.641395, 4.56084, 17.7436 ];

dai_vf_time = [ 0.0057147, 0.0229099, 0.087495, 0.281235, 1.49731, 7.37181 ];
dai_runtime = bfcull_time + dai_vf_time;

sai_vf_time = [ 0.0067083, 0.0210774, 0.107661, 0.427278, 2.49272, 9.30337 ];
sai_runtime = bfcull_time + sai_vf_time;

N = [ 394240, 3920000, 23831808, 122988096, 1005132800, 3805401600 ];
N_p1 = [ 640, 1960, 4928, 11088, 31808, 61776 ];
N_p2 = [ 616, 2000, 4836, 11092, 31600, 61600 ];

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);


figure(1)
loglog(N, dai_errors, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_errors, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Absolute Error")
legend("DAI","SAI")
xlim([1e5,1e10])
xticks([1e5,1e6,1e7,1e8,1e9,1e10])
set(gca,"XTickLabelRotation",0)
ylim([1e-5,1e-2])
yticks([1e-5,1e-4,1e-3,1e-2])
set(gca, "FontSize", 18)
set(figure(1),'Units','centimeters')
set(figure(1),'PaperUnits','centimeters')
set(figure(1),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "cylinders-r=0.125-r=0.25-convergence.pdf";
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
xlim([1e5,1e10])
xticks([1e5,1e6,1e7,1e8,1e9,1e10])
set(gca,"XTickLabelRotation",0)
ylim([1e-2,1e2])
yticks([1e-2,1e-1,1e0,1e1,1e2])
set(gca, "FontSize", 18)
set(figure(2),'Units','centimeters')
set(figure(2),'PaperUnits','centimeters')
set(figure(2),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "cylinders-r=0.125-r=0.25-runtime.pdf";
pause(1.5)
exportgraphics(figure(2), full_file_name)
hold off