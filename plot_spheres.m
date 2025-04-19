clear all
close all
clc

set(groot, "defaultAxesTickLabelInterpreter", "latex")
set(groot, "defaulttextInterpreter", "latex")
set(groot, "defaultLegendInterpreter","latex")

output_path = "test_outputs/pdfs/";
paper_size = 12;

%!-- SPHERES (r=1 -> r=3)

dai_numeric = [ 1.04425369223099, 1.01149067960918, 1.00295624723579, 1.00072692303148, 1.00018216953377, 1.00004757432872 ];
sai_numeric = [ 0.981121317744366, 0.995822164169393, 0.999106979107552, 0.999764755406502, 0.99994167603952, 0.999987466395445 ];
analytic = 1;

bfcull_time = [ 0.0069683, 0.0095329, 0.0202768, 0.157226, 1.99733, 30.0337 ];

dai_vf_time = [ 0.0024447, 0.0037694, 0.0116934, 0.100325, 0.726656, 11.6124 ];
dai_runtime = bfcull_time + dai_vf_time;

sai_vf_time = [ 0.0026255, 0.0047332, 0.0163002, 0.112152, 1.65946, 21.831 ];
sai_runtime = bfcull_time + sai_vf_time;

N = [ 6400, 102400, 1638400, 26214400, 419430400, 2415919104 ];
N_p = [ 80, 320, 1280, 5120, 20480, 81920 ];
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
xlim([1e3,1e10])
xticks([1e3,1e4,1e5,1e6,1e7,1e8,1e9,1e10])
set(gca,"XTickLabelRotation",0)
ylim([1e-5,1e-1])
yticks([1e-5,1e-4,1e-3,1e-2,1e-1])
set(gca, "FontSize", 18)
set(figure(1),'Units','centimeters')
set(figure(1),'PaperUnits','centimeters')
set(figure(1),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "spheres-r=1-r=3-convergence.pdf";
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
xlim([1e3,1e10])
xticks([1e3,1e4,1e5,1e6,1e7,1e8,1e9,1e10])
set(gca,"XTickLabelRotation",0)
ylim([1e-3,1e2])
yticks([1e-3,1e-2,1e-1,1e0,1e1,1e2])
set(gca, "FontSize", 18)
set(figure(2),'Units','centimeters')
set(figure(2),'PaperUnits','centimeters')
set(figure(2),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "spheres-r=1-r=3-runtime.pdf";
pause(1.5)
exportgraphics(figure(2), full_file_name)
hold off