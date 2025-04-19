clear all
close all
clc

set(groot, "defaultAxesTickLabelInterpreter", "latex")
set(groot, "defaulttextInterpreter", "latex")
set(groot, "defaultLegendInterpreter","latex")

output_path = "test_outputs/pdfs/";
paper_size = 12;

%! -- EMITTER REFINEMENT PERPENDICULAR PLATES SHARING (1x1)
%TODO REPLACE THIS WITH NEW RECTANGLE GENERATION

dai_numeric = [ 0.211632649515177, 0.202099959466053, 0.200309685950562, 0.199769446613668, 0.199620112971736 ];
sai_numeric = [ 0.200149624038132, 0.200021419384965, 0.200037976684939, 0.200041533922361, 0.20004364952502 ];

analytic = 0.200043776075403;

N = [ 1156, 7514, 31314, 125188, 782034 ];

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);


figure(1)
loglog(N, dai_errors, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_errors, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)


dai_numeric = [0.211632649515177, 0.202380482650054, 0.201188740868883, 0.20061638550097, 0.200262786840401]; % 
sai_numeric = [0.200149624038132, 0.200021419384941, 0.200037976684927, 0.200041533922356, 0.200043649525026]; % 

analytic = 0.200043776075403;

N = [1156, 48841, 848241, 13557124, 529046001];

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
ylim([1e-8,1e-1])
yticks([1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "TEMPORARY-sharing-perp-plates-1x1-e-only-convergence.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off










%! -- PERPENDICULAR PLATES (SHARING) (1x1)
%!  DISTMESH GENERATION

dai_numeric = [0.211632649515177, 0.202380482650054, 0.201188740868883, 0.20061638550097, 0.200262786840401, 0.200375538830306];
sai_numeric = [0.200149624038132, 0.200021419384941, 0.200037976684927, 0.200041533922356, 0.200043649525026, 0.200043426686355];

analytic = 0.200043776075403;

N = [1156, 48841, 848241, 13557124, 529046001, 3454735729];

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);


dai_vf_time = [ 0.0047049, 0.0060489, 0.0148585, 0.116411, 3.2951, 21.2077]; %
dai_runtime = dai_vf_time;

sai_vf_time = [ 0.005784, 0.0056688, 0.0200691, 0.150916, 4.49884, 28.8508 ]; %
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
ylim([1e-8,1e-1])
yticks([1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "sharing-perp-plates-1x1-convergence.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
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
ylim([1e-3,1e2])
yticks([1e-3,1e-2,1e-1,1e0,1e1,1e2])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "sharing-perp-plates-1x1-runtime.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off








%! -- PERPENDICULAR PLATES (SHARING) (1x1)
%! NEW MESH GENERATION

dai_numeric = [ 0.222544395891801 , 0.205467402592189 , 0.202282025842643 , 0.201174854595616 , 0.200800522530535 ];
sai_numeric = [ 0.19984147018417 , 0.200032387226767 , 0.200041845759303 , 0.200043283918191 , 0.200043555887817 ];
dai_vf_time = [ 0.010596 , 0.013923 , 0.203448 , 2.5122 , 12.4259 ];
sai_vf_time = [ 0.0110922 , 0.0197225 , 0.26743 , 3.58879 , 17.0575 ];
N = [ 2500 , 777924 , 27060804 , 416241604 , 2079542404 ];

analytic = 0.200043776075403;

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);

dai_runtime = dai_vf_time;
sai_runtime = sai_vf_time;


figure(4)
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
ylim([1e-8,1e-1])
yticks([1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "sharing-perp-plates-1x1-convergence-new-rectangles.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off

figure(5)
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
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "sharing-perp-plates-1x1-runtime-new-rectangles.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off









%! -- EMITTER REFINEMENT PERPENDICULAR PLATES NONSHARING (1x1)

dai_numeric = [ 0.157706823874397, 0.156140983370564, 0.155890483669088, 0.155826329466988, 0.155807421472149, 0.155805252586253 ];
sai_numeric = [ 0.155706711004898, 0.154467225181274, 0.154275611934348, 0.1542250792057, 0.154209871844401, 0.154208127372574 ];

analytic = 0.154206868494109;

N = [ 1156, 7514, 31314, 125188, 782034, 1998418 ];

dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);


figure(6)
loglog(N, dai_errors, "o:k", "MarkerSize", 10, "LineWidth", 3)
hold on
loglog(N, sai_errors, "s--k", "MarkerSize", 10, "MarkerFaceColor", "k", "LineWidth", 3)


dai_numeric = [0.157706823874397, 0.15479907479484, 0.154353038778517, 0.154244229169982, 0.154212915088377, 0.15420931251383];
sai_numeric = [0.155706711004898, 0.154467225181253, 0.154275611934338, 0.154225079205695, 0.154209871844406, 0.154208127372573];

analytic = 0.154206868494109;

N = [1156, 48841, 848241, 13557124, 529046001, 3454735729];

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
ylim([1e-6,1e-2])
yticks([1e-6,1e-5,1e-4,1e-3,1e-2])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "nonsharing-perp-plates-1x1-e-only-convergence.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off








%! -- PERPENDICULAR PLATES (NONSHARING) (1x1 offset 0.1)

dai_numeric = [0.157706823874397, 0.15479907479484, 0.154353038778517, 0.154244229169982, 0.154212915088377, 0.15420931251383];
sai_numeric = [0.155706711004898, 0.154467225181253, 0.154275611934338, 0.154225079205695, 0.154209871844406, 0.154208127372573];
analytic = 0.154206868494109;


N = [1156, 48841, 848241, 13557124, 529046001, 3454735729];
N_p = [34, 221, 921, 3682, 23001, 58777];


dai_errors = abs(dai_numeric - analytic);
sai_errors = abs(sai_numeric - analytic);


dai_vf_time = [ 0.0114131, 0.0090086, 0.01466, 0.118835, 3.23575, 20.4536 ];
dai_runtime = dai_vf_time;

sai_vf_time = [ 0.0049061, 0.0093631, 0.0225732, 0.150305, 4.66256, 39.3182 ];
sai_runtime = sai_vf_time;


figure(7)
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
ylim([1e-6,1e-2])
yticks([1e-6,1e-5,1e-4,1e-3,1e-2])
set(gca, "FontSize", 18)
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "nonsharing-perp-plates-1x1-convergence.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off

figure(8)
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
set(gcf,'Units','centimeters')
set(gcf,'PaperUnits','centimeters')
set(gcf,'PaperSize',[1.1*paper_size, paper_size])
full_file_name = output_path + "nonsharing-perp-plates-1x1-runtime.pdf";
pause(0.5)
exportgraphics(gcf, full_file_name)
hold off