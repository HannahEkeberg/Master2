clear all; clc;


% make some gamma ray energies for plotiing
xp= 30:2500;

% Select efficiency calibration matrix
effcal_new = '../../Calibration/eff_HPGE2_45.mat'   %npat generated
effcal_old = '../../Program/efficiency_csv/eff_room131_50_old.mat' %own 

[efficiency_new, unc_efficiency_new, ~, ~] = efficiency_calibration(xp, effcal_new);
[efficiency_old, unc_efficiency_old, ~, ~] = efficiency_calibration(xp, effcal_old);


%Plotting uncertainty band
% plot(xp, efficiency_old, 'r', xp, efficiency_new,   'b' , ...
%      xp, efficiency_old + unc_efficiency_old, 'r--', xp, efficiency_new + unc_efficiency_new, 'b--', ...
%      xp, efficiency_old - unc_efficiency_old, 'r--', xp, efficiency_new - unc_efficiency_new, 'b--')
% xlabel('Gamma-Ray Energy (keV)')
% ylabel('Detector  Efficiency')
% legend('Old Efficiencies', 'New Efficiencies')

% OR

% Plotting percent uncertainty
plot(xp, 100.*unc_efficiency_old./ efficiency_old,    xp, 100.*unc_efficiency_new./ efficiency_new)
xlabel('Gamma-Ray Energy (keV)')
ylabel('Percent Uncertainty in Efficiency')
legend('Old Efficiencies', 'New Efficiencies')