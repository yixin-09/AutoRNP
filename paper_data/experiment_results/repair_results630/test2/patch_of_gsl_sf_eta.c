static double array_x_sf_eta_0[6] = {
-2.000071592196258852e+00,
-2.000053694147194250e+00,
-2.000017898049064602e+00,
-2.000008949024532079e+00,
-2.000004474512266039e+00,
-2.000000000000000000e+00,
};
static double array_y_sf_eta_0[6] = {
-1.525878904024915260e-05,
-1.144415072301714026e-05,
-3.814756201925431066e-06,
-1.907383012605151193e-06,
-9.536927342178301693e-07,
0.000000000000000000e+00,
};
static double array_e_y_sf_eta_0[6] = {
-1.144415072301714026e-05,
-7.629473109872863363e-06,
-7.629473109872863363e-06,
-3.814756201925431066e-06,
-1.907383012605151193e-06,
-9.536927342178301693e-07,
};
static double array_detla_sf_eta_0[6] = {
9.464940620336914075e-17,
9.465038121737941838e-17,
9.465135620856727210e-17,
9.465208743769416439e-17,
9.465245304726519953e-17,
9.465269678507737792e-17,
};
static double array_idx_sf_eta_0[7] = {
0.000000000000000000e+00,
4.030282354900000000e+10,
8.060564709900000000e+10,
1.209084706480000000e+11,
1.410598824230000000e+11,
1.511355883100000000e+11,
1.612112941970000000e+11,
};
static double array_maxE_sf_eta_0[6] = {
6.133523423437223232e-02,
6.133379853314810393e-02,
6.133236285916460889e-02,
6.133128610892739363e-02,
6.133074772026424204e-02,
6.133038883273744107e-02,
};
double accuracy_improve_patch_of_gsl_sf_eta_0(double x)
{
 long int n = 161211294198;
 int len_glob = 6;
 double ulp_x = 4.440892098500626e-16;
 double x_0 = -2.000071592196259;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_eta_0[idx])&&(n_x<array_idx_sf_eta_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_eta_0[idx+1])*(n_x-array_idx_sf_eta_0[idx])*array_maxE_sf_eta_0[idx];
         return (x-array_x_sf_eta_0[idx])/ulp_x*array_detla_sf_eta_0[idx]+array_y_sf_eta_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_eta_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_eta_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_eta_0[idx]){
         return array_y_sf_eta_0[idx];
     }
     else{
         return array_e_y_sf_eta_0[idx];
     }
 }
}
static double array_x_sf_eta_1[6] = {
-1.999999999999999778e+00,
-1.999995525672073615e+00,
-1.999991051344147452e+00,
-1.999982102688295127e+00,
-1.999964205376590476e+00,
-1.999946308064885825e+00,
};
static double array_y_sf_eta_1[6] = {
4.732640932675400909e-17,
9.536558999263838183e-07,
1.907314255404864253e-06,
3.814638333102613282e-06,
7.629315955058903007e-06,
1.144403286499651375e-05,
};
static double array_e_y_sf_eta_1[6] = {
9.536558999263838183e-07,
1.907314255404864253e-06,
3.814638333102613282e-06,
7.629315955058903007e-06,
1.144403286499651375e-05,
1.525878906199576806e-05,
};
static double array_detla_sf_eta_1[6] = {
4.732647025822125214e-17,
4.732659212068031395e-17,
4.732677491294262151e-17,
4.732714049247531865e-17,
4.732762792234382008e-17,
4.732811534080226202e-17,
};
static double array_idx_sf_eta_1[7] = {
0.000000000000000000e+00,
2.015058158100000000e+10,
4.030116316200000000e+10,
8.060232632400000000e+10,
1.612046526480000000e+11,
2.418069789720000000e+11,
3.224093052960000000e+11,
};
static double array_maxE_sf_eta_1[6] = {
6.133002991386875269e-02,
6.132967104965710708e-02,
6.132913265285300231e-02,
6.132805595444266317e-02,
6.132662036008804801e-02,
6.132518477631097864e-02,
};
double accuracy_improve_patch_of_gsl_sf_eta_1(double x)
{
 long int n = 322409305297;
 int len_glob = 6;
 double ulp_x = 2.220446049250313e-16;
 double x_0 = -1.9999999999999998;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_eta_1[idx])&&(n_x<array_idx_sf_eta_1[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_eta_1[idx+1])*(n_x-array_idx_sf_eta_1[idx])*array_maxE_sf_eta_1[idx];
         return (x-array_x_sf_eta_1[idx])/ulp_x*array_detla_sf_eta_1[idx]+array_y_sf_eta_1[idx]+compen;
     }
     else if(n_x<array_idx_sf_eta_1[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_eta_1[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_eta_1[idx]){
         return array_y_sf_eta_1[idx];
     }
     else{
         return array_e_y_sf_eta_1[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_eta(double x)
{
if(x<=-2.0){
 return accuracy_improve_patch_of_gsl_sf_eta_0(x);
}
if(x<=-1.9999284107531812){
 return accuracy_improve_patch_of_gsl_sf_eta_1(x);
}
}
