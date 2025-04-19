clear all
close all
clc

set(groot, "defaultAxesTickLabelInterpreter", "latex")
set(groot, "defaulttextInterpreter", "latex")
set(groot, "defaultLegendInterpreter","latex")

output_path = "test_outputs/pdfs/";
paper_size = 12;

%! -- BLOCKING BVH (sphere to inner cylinder) (using l3 blocker)

dai_numeric = [ 0.000720907710896718, 0.000635775216166577, 0.000615795508111154 ];
sai_numeric = [ 0.000720934189132695, 0.000635781718937571, 0.000615797847646431 ];

analytic = 6.189692152239722e-04;

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);

bvh_gen_time = 0.280188;

bfcull_time = [ 0.0062275, 0.00958, 0.0395491 ];
blocking_time = [ 0.60031, 5.34918, 44.9461 ];

dai_vf_time = [ 0.0004183, 0.0013385, 0.0069409 ];
dai_runtime = bvh_gen_time + bfcull_time + blocking_time + dai_vf_time;

sai_vf_time = [ 0.0006969, 0.0014585, 0.0075412 ];
sai_runtime = bvh_gen_time + bfcull_time + blocking_time + sai_vf_time;

N = [ 51200, 627200, 6307840 ];

figure(1)
loglog(N, dai_errors, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_errors, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Absolute Error")
legend("DAI","SAI")
xlim([1e4,1e7])
xticks([1e4,1e5,1e6,1e7])
set(gca,"XTickLabelRotation",0)
ylim([1e-6,1e-3])
yticks([1e-6,1e-5,1e-4,1e-3])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "bvh-l3-blocking-r=3-r=0.125-r=0.25-convergence.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off



figure(2)
loglog(N, dai_runtime, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_runtime, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Runtime [s]")
legend("DAI","SAI","Location","northwest")
xlim([1e4,1e7])
xticks([1e4,1e5,1e6,1e7])
set(gca,"XTickLabelRotation",0)
ylim([1e-1,1e2])
yticks([1e-1,1e0,1e1,1e2])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "bvh-l3-blocking-r=3-r=0.125-r=0.25-runtime.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off








%! -- BLOCKING NAIVE (sphere to inner cylinder) [using L6 cylinder as blocker]

dai_numeric = [ 0.000722707922436342, 0.000637422025970147, 0.000617251445274479, 0.00061401919280487 ];
sai_numeric = [ 0.000732008410932809, 0.000637428065224969, 0.000617253645049228, 0.000614020155894994 ];

analytic = 6.189692152239722e-04;

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);

bfcull_time = [ 0.0062275, 0.00958, 0.0395491, 0.295755 ];
blocking_time = [ 0.873529, 9.9989, 95.9502, 810.792 ];

dai_vf_time = [ 0.0024794, 0.0033877, 0.0105949, 0.0347767 ];
dai_runtime = bfcull_time + blocking_time + dai_vf_time;

sai_vf_time = [ 0.0029003, 0.0035758, 0.0086401, 0.0489613 ];
sai_runtime = bfcull_time + blocking_time + sai_vf_time;

N = [ 51200, 627200, 6307840, 56770560];%, 651427840 ];
N_p1 = [ 80, 320, 1280, 5120, 20480  ];
N_p2 = [ 640, 1960, 4928, 11088, 31808 ];

figure(3)
loglog(N, dai_errors, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_errors, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Absolute Error")
legend("DAI","SAI")
xlim([1e4,1e8])
xticks([1e4,1e5,1e6,1e7,1e8])
set(gca,"XTickLabelRotation",0)
ylim([1e-6,1e-3])
yticks([1e-6,1e-5,1e-4,1e-3])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "naive-l6-blocking-r=3-r=0.125-r=0.25-convergence.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off

figure(4)
loglog(N, dai_runtime, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_runtime, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Runtime [s]")
legend("DAI","SAI","Location","northwest")
xlim([1e4,1e8])
xticks([1e4,1e5,1e6,1e7,1e8])
set(gca,"XTickLabelRotation",0)
ylim([1e-1,1e3])
yticks([1e-1,1e0,1e1,1e2,1e3])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "naive-l6-blocking-r=3-r=0.125-r=0.25-runtime.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off





%! --- BLOCKING RUNTIME COMPARISON (USING L3 BLOCKER)

naive_blocking_time = [ 0.081131, 0.817996, 7.81749 ];
bvh_blocking_time = [ 0.60031, 5.34918, 44.9461 ];
N = [ 51200, 627200, 6307840];

figure(5)
loglog(N, naive_blocking_time, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, bvh_blocking_time, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)
grid on
xlabel("Number of Element Pairs")
ylabel("Runtime [s]")
legend("Naive","BVH","Location","northwest")
xlim([1e4,1e7])
xticks([1e4,1e5,1e6,1e7])
set(gca,"XTickLabelRotation",0)
ylim([1e-2,1e2])
yticks([1e-2,1e-1,1e0,1e1,1e2])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "l3-blocking-r=3-r=0.125-r=0.25-runtime-comparison.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off