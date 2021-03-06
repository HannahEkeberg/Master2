clear all; clc;
fclose('all');

% Load key energies
load fe_key_energies.mat
load cu_key_energies.mat
load ni_key_energies.mat
load ir_key_energies.mat
%load only_mon_key_ener/gies.mat

% Load gamma line half-lives and intensities
load fe_glines.mat
load cu_glines.mat
load ni_glines.mat
load ir_glines.mat
%load only_mon_glines.mat



% Load file names
%u_fn  = textscan(fopen('u_fnames.txt'),'%s');
ir_fn = textscan(fopen('ir_fnames.txt'),'%s');
cu_fn = textscan(fopen('cu_fnames.txt'),'%s');
ni_fn = textscan(fopen('ni_fnames.txt'),'%s');
% ni_fn = textscan(fopen('ni_fnames-kopi.txt'),'%s');
fe_fn = textscan(fopen('fe_fnames.txt'),'%s');
%mon_fn = textscan(fopen('mon_fnames.txt'),'%s');
%only_mon_fn = textscan(fopen('only_mon_fnames.txt'),'%s');






% Set areal densities and their uncertainties
%u_rhodrs =  [208.705    168.473];
ir_rhodrs = [55.9950   55.6010   55.6430   56.0000   55.1610   55.7310   56.6850   58.0300   56.6690   55.0650];  %mass densities
cu_rhodrs = [22.3380   22.3250   22.3130   22.2840   22.4430   22.3960   22.3200   22.4010   22.4250   22.3140];
ni_rhodrs = [22.7720   23.1180   22.3380   20.7040   21.7680   22.8610   23.0920   22.4090   21.7410   23.0930];
fe_rhodrs = [20.030    20.017    19.948];
%unc_u_rhodrs = [0.599   0.483];
unc_ir_rhodrs = [0.053,0.238,0.121,0.109,0.081,0.088,0.085,0.130,0.043,0.055];
unc_cu_rhodrs = [0.048,0.028,0.043,0.027,0.028,0.012,0.014,0.033,0.041,0.047];
unc_ni_rhodrs = [0.138,0.096,0.066,0.068,0.045,0.123,0.078,0.124,0.073,0.024];
unc_fe_rhodrs = [0.110,0.034,0.114];


%%
clc;

% Choose files for analysis
fitzpeaks_reports = ni_fn;
key_energies = ni_key_energies;
glines = ni_glines;
EoB_Time = '26-Feb-2019 00:32:00'
rhodrs = ni_rhodrs;
mu_attenuation = load('ni_xcom.txt');
unc_rhodrs = unc_ni_rhodrs;


% Test new fitzpeaks_parser wrapper function

% data_mat  = fitzpeaks_parser(filename_list, key_energies, gamma_lines, EoB_Time, attenuation_data, rhodrs, unc_rhodrs)
%Calling the fitzpeakz parser 
output = fitzpeaks_parser(string(fitzpeaks_reports{1}), key_energies, glines, EoB_Time, mu_attenuation, rhodrs, unc_rhodrs);



%%

% Load parsed matrices from output of previous section
% load ni_mat.mat;
% load fe_mat.mat;
% load cu_mat.mat;
% load ir_mat.mat;


% Matrix format:
%
% Each row corresponds to a key energy, from the ZZZ_key_energies matrices,
%  or from your energy assignments list
%
% Each column (one spectrum) corresponds to the GammaCounts objects containing
% info about the peaks in that spectrum



% Set foils for analysis
data = output;


% Rows for each decay product:
%rows_61Cu = [1 6 10 14 15 16 25 ];

% % 33MeV Nickel foils:
rows_Ni_52mMn = [70];   %check, check
% rows_Ni_52Mn = [27,42,60,64,71];  %check
rows_Ni_52Mn = [27,42,60,71];  %check
rows_Ni_52gMn = [27,42,60];  %check
rows_Ni_54Mn = [35]; %check
%rows_Ni_55Co = [3,13,15,18,30,34,41,46,57,63,67,69,84,97,104];   %check
rows_Ni_55Co = [13,18,30,41,57,63,67,97];   %check

% rows_Ni_56Co = [29,45,55,59,66,82,90,91,92,99,101];  %check
rows_Ni_56Co = [29,45,55,90,91,92, 106];  %check
% rows_Ni_56Co = [29,45,55,59,82,90];  %check
% rows_Ni_56Co = [29,45,55,90, 106];  %check
% rows_Ni_56Co = [29,55, 106,59];  %check
% rows_Ni_56Co = [106];
rows_Ni_56Mn = [ 106,107,108];  %check
%rows_Ni_56Mn = [ 107,108];  %check
%rows_Ni_56Ni = [7,8,16,28,32,74];  %check
rows_Ni_56Ni = [7,16,28,32,74];  %check
%rows_Ni_57Co = [4,6,26]; %check
rows_Ni_57Co = [4,6]; %check
%rows_Ni_57Ni = [12,25,40,49,58,68,80,81,86,87,95,103]; %check
%rows_Ni_57Ni = [68,81,87]; 
rows_Ni_57Ni = [81,87,103]; 
rows_Ni_58Co = [31,38,77];   %check
rows_Ni_59Fe = [61];%check

rows_Ni_61Co = [111,112,113];
% rows_Ni_60Cu = [14,17,23,36,43,44,48,52,62,83,85,88,89,93,96,99,101,102]; %check
%rows_Ni_60Cu = [14,17,23,43,48,52,62,83,85,89,93,96,99,101,102]; %check
%rows_Ni_60Co = [1]; %check
%rows_Ni_60Co = [109, 110]; %check


% rows_Ni_61Cu = [2,9,11,19,20,22,24,33,37,39,47,50,51,54,56,72,76,79,94]; %check
rows_Ni_61Cu = [9,11,19,20,22,24,33,37,39,47,51,54,56,72]; %check

rows_Ni_64Cu = [65]; %check
%rows_Ni_65Ni = [10,21,53,73,75,78]; %check
rows_Ni_65Ni = [10,73,75,78]; %check





% % 33MeV Copper foils:
%rows_Cu_52Mn = [20,23,34,39]; %check
rows_Cu_52gMn = [20,23,34,39]; %check
rows_Cu_56Co = [22,25,31,42,44,47];  %check
rows_Cu_57Co = [3,15]; %check
rows_Cu_57Ni = [36]; %check
rows_Cu_58Co = [21];  %check
%rows_Cu_59Fe = [10, 26, 32]; %check
rows_Cu_59Fe = [26, 32]; %check
rows_Cu_60Co = [29,33];%check
rows_Cu_61Co = [2]; % check
% rows_Cu_61Cu = [2,8,18,30]; %check
rows_Cu_61Cu = [8,18,30]; %check
rows_Cu_62Zn = [1,4,6,7,9,11,12,14,16,17]; %check
% rows_Cu_63Zn = [5,13,19,24,28,37,38,41,43,45,46]; %check 
rows_Cu_63Zn = [13,19,24]; %check 
rows_Cu_64Cu = [35]; %check
rows_Cu_65Ni = [40]; %check
rows_Cu_65Zn = [27]; %check

rows_Cu_56Mn = [48];
rows_Cu_54Mn = [49];


% % 33MeV Iron foils:
rows_Fe_48V = [24,26,37];  %check
rows_Fe_51Cr = [5]; %check
rows_Fe_51Mn = [12]; %check
rows_Fe_52mMn = [44]; %check
rows_Fe_52Mn = [6,11,19,23,35,39,45]; %check
rows_Fe_53Fe = [7]; %check
rows_Fe_54Mn = [17]; %check
rows_Fe_55Co = [1,8,14,22,38,42,43,55,16,50,54]; %check

rows_Fe_56Co = [4,9,10,13,18,20,21,25,27,28,30,31,32,33,34,40,41,46,47,48,49,51,52,53]; %check
% rows_Fe_56Co = [10,13,18,25,27,28,30,32,34,40,41,46,47,48,49,51,52,53];
% rows_Fe_56Co = [4,9,10,20,21,25,27,30,31,32,33,40,41,46,47,48,49,51,52,53]; %check
rows_Fe_57Co = [2,3];%check
rows_Fe_58Co = [15]; %check
rows_Fe_59Fe = [29,36]; %check
%rows_55Co = [];

rows_Fe_56Mn = [57,58,59];


% % 33MeV Iridium foils:
rows_Ir_183Ta = [23,38]; %check
% rows_Ir_183Ta = [38]; %check
% rows_Ir_186Re = [8,12]; %check
rows_Ir_186Re = [12]; %check
% rows_Ir_186Ta = [20,58]; %check
% rows_Ir_186Ta = [20]; %check
% rows_Ir_187W = [54,68,73,9]; %check
rows_Ir_187W = [54,73]; %check
% rows_Ir_188Ir = [78,89,92,93,94]; %check
rows_Ir_188Ir = [89,92,93]; %check
rows_Ir_188mRe = [1,5]; %check
% rows_Ir_188Pt = [17,42,48,53]; %check
rows_Ir_188Pt = [17,42]; %check
rows_Ir_188Re = [77,82]; %check
%rows_Ir_188Re = [77, 106]; %check
%rows_Ir_189Ir = [3,21, 100, 101, 102]; %check
rows_Ir_189Ir = [21,102]; %check
% rows_Ir_189Ir = [21, 102]; %check
%rows_Ir_189Pt = [2,6,22,31,35,60,75]; %check
rows_Ir_189Pt = [2,6,22,35,75]; %check
%rows_Ir_189Re = [13,14,16,62]; %check
%rows_Ir_189Re = [13,14,62]; %check
%rows_Ir_189Re = [62]; %check
rows_Ir_189Re = [62, 103, 104, 105]; %check
%rows_Ir_189Re = [62];

rows_Ir_189W = [24,47,80]; %check
%rows_Ir_190Ir = [27,29,41,44,49,76,84]; %check
rows_Ir_190Ir = [29,41,84]; %check
rows_Ir_190mRe = [7,72]; %check
%rows_Ir_190Re = [50,79,88,90]; %check
rows_Ir_190Re = [50,79,88]; %check
%rows_Ir_191Pt = [4,15,25,37,39,45,51,59,70]; %check
rows_Ir_191Pt = [15,37,45,51,59,70]; %check
% rows_Ir_192Ir = [11,18,19,26,30,33,34,40,46,52,56,57,63,66,67,81,85]; %check
% rows_Ir_192Ir = [18,30,40,46,52,57,67,85]; %check
rows_Ir_192Ir = [18,40,46,52,57,67,85]; %check
% rows_Ir_192Ir = [52]; %check
rows_Ir_193mPt = [10,98]; %check
% rows_Ir_193mPt = [10]; %check

%rows_Ir_194Ir = [28,32,64,69,71,83,86,87,91];%check
% rows_Ir_194Ir = [28,32,64,83,86,91];%check
rows_Ir_194Ir = [28,83,91];%check


rows_Ir_194m2Ir = [55,61,74]; %check
% rows_Ir_194m2Ir = [43]; %check
% rows_Ir_194m2Ir = [61,74]; %check
rows_Ir_191Os = [107]; %check
%rows_Ir_190m2Ir = [108, 109, 110, 111]; %check
rows_Ir_190m2Ir = [109,110]; %check

%rows_Ir_193Os = [112, 113, 114, 115, 116, 117, 118]; %check
rows_Ir_193Os = [112, 113, 116, 117]; %check



% Select rows to plot
% varToStr = @(x) inputname(1);
rows = rows_Ni_61Cu;
outName = '../csv/Ni_61Cu';
% rows = 12;
% Find rows for the desired decay product
selected_rows = data(rows,:);


% Gate on foil energy 
% 
% energy = 0; % Show all foils in one plot (not for analysis!)
% 
% loop over all energies for a foil type
for energy = 128:100:1028   % Just Nickel
% for energy = 129:100:1029   % Just Copper
% for energy = 126:100:326   % Just Iron
% for energy = 177:100:1077   % Just Iridium
% 
%  for energy = 126   % debug mode
    if energy==0
        % Return all rows for plotting
        gammas = selected_rows;
    else
        % Oly return rows which match the desired energies
        indices = find([selected_rows.Mass] == energy);   
        %Selected_rows =all objects corresponding to key energies.
        %.Mass gives an array of mass number in every spectrum in those rows. 
        %Where in the big matrix where you have a count of one of your key
        %energies with the foil of your mass number. 
        gammas =  selected_rows(indices);
        %Finding the gamma objects belonging to those indices. 
    end
    
    % Pull the data from the GammaCounts objects
    
    % check for Co56 background contamination on IDMs(+HPGE) in Cave 4C
    if isequal(rows, rows_Ni_56Co)
        unwanted_indices = zeros(1,length(gammas));
        % we are looking at 56CO
        for gamma_index=1:length(gammas)
            obj = gammas(1,gamma_index);
            if obj.TimeSinceEoB < 25.0
                if (obj.EGamma == key_energies(rows_Ni_56Mn(1))) || (obj.EGamma == key_energies(rows_Ni_56Mn(2))) || (obj.EGamma == key_energies(rows_Ni_56Mn(3)))
                    unwanted_indices(gamma_index) = 1;
%                 background_count_rate = 2.8338e-02;
%                 % get the 1238 keV count rate
%                 contaminated_count_rate = obj.NumberOfCounts
%                 % get 
                end
            end
        end
%         gammas = gammas(1,wanted_indices);
    gammas = gammas(1,unwanted_indices==0);
    end
   
    
    
    
    activities     = [gammas.Activity];
    delta_ts       = [gammas.TimeSinceEoB];
    unc_activities = [gammas.UncertaintyActivity];
    
    % also pull out number of decays
    decays     = [gammas.NumberofDecays];
    unc_decays = [gammas.UncertaintyNumberofDecays];
    live_times = [gammas.LiveTime];
    
    errorbar(delta_ts,activities',unc_activities','.')
    
    if  length(gammas) > 0
        outfile =  [delta_ts; activities; unc_activities; decays; unc_decays; live_times]';    %Writing to the csv. '=tranpose
    else
        outfile =  [0; 0; 1; 0; 0; 1]';    %Writing to the csv. '=tranpose
    end
    
    %     Dump to csv for python / gnuplot
    %     Turn this line on to write files out!
    csvwrite([outName '_' num2str(energy) '.dat'],outfile);  %Saving the csv file 
end
