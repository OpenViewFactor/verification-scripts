clear all
close all
clc

set(groot, "defaultAxesTickLabelInterpreter", "latex")
set(groot, "defaulttextInterpreter", "latex")
set(groot, "defaultLegendInterpreter","latex")

output_path = "test_outputs/pdfs/";
paper_size = 12;

%! -- EMITTER REFINEMENT PARALLEL PLATES (1x1)

dai_numeric = [ 0.20212363219738, 0.201135875502503, 0.20100549515962, 0.200975987591356, 0.200967864349643, 0.200966927642102 ];   % single refinement
sai_numeric = [ 0.200966328733284, 0.199992157681057, 0.199863539076925, 0.199834425937356, 0.199826410889325, 0.199825486650222 ];

analytic = 0.199824895698387;

N = [ 1156, 7514, 31314, 125188, 782034, 1998418 ];

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);


figure(1)
loglog(N, dai_errors, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_errors, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)


dai_numeric = [0.20212363219738, 0.200159756748512, 0.199902200140395, 0.199843957245614, 0.199827926107253, 0.199826077606153];    % both refined for comparison
sai_numeric = [0.200966328733284, 0.199992157681007, 0.199863539076901, 0.199834425937343, 0.199826410889331, 0.199825486650218];

analytic = 0.199824895698387;

N = [1156, 48841, 848241, 13557124, 529046001, 3462145600];

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);

loglog(N, dai_errors, ":", "Color",[0,0,0,0.3], "MarkerSize", 10, "LineWidth", 3)
loglog(N, sai_errors, "--", "Color",[0,0,0,0.3], "MarkerFaceColor", "k", "MarkerSize", 10, "LineWidth", 3)
hold off
grid on
xlabel("Number of Element Pairs")
ylabel("Absolute Error")
legend("DAI - single refined","SAI - single refined", "DAI - both refined", "SAI - both refined")
xlim([1e2,1e10])
xticks([1e2,1e3,1e4,1e5,1e6,1e7,1e8,1e9,1e10])
set(gca,"XTickLabelRotation",0)
ylim([1e-7,1e-2])
yticks([1e-7,1e-6,1e-5,1e-4,1e-3,1e-2])
set(gca, "FontSize", 18)
set(figure(1),'Units','centimeters')
set(figure(1),'PaperUnits','centimeters')
set(figure(1),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "par-plates-1x1-e-only-convergence.pdf";
pause(1.5)
exportgraphics(figure(1), full_file_name)
hold off






%! -- PARALLEL PLATES (1x1)

dai_numeric = [0.20212363219738, 0.200159756748512, 0.199902200140395, 0.199843957245614, 0.199827926107253, 0.199826077606153];
sai_numeric = [0.200966328733284, 0.199992157681007, 0.199863539076901, 0.199834425937343, 0.199826410889331, 0.199825486650218];

analytic = 0.199824895698387;

N = [1156, 48841, 848241, 13557124, 529046001, 3462145600];
N_p = [34, 221, 921, 3682, 23001, 58777];

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);


dai_vf_time = [ 0.0052841, 0.0084617, 0.0176876, 0.111636, 3.24421, 19.9769 ]; 
dai_runtime = dai_vf_time;

sai_vf_time = [ 0.0053738, 0.0068895, 0.0199872, 0.155469, 4.8668, 28.9002 ];
sai_runtime = sai_vf_time;


figure(2)
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
set(figure(2),'Units','centimeters')
set(figure(2),'PaperUnits','centimeters')
set(figure(2),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "par-plates-1x1-convergence.pdf";
pause(1.5)
exportgraphics(figure(2), full_file_name)
hold off


figure(3)
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
ylim([1e-7,1e-2])
ylim([1e-3,1e2])
yticks([1e-3,1e-2,1e-1,1e0,1e1,1e2])
set(gca, "FontSize", 18)
set(figure(3),'Units','centimeters')
set(figure(3),'PaperUnits','centimeters')
set(figure(3),'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "par-plates-1x1-runtime.pdf";
pause(1.5)
exportgraphics(figure(3), full_file_name)
hold off