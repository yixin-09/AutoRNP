static double array_x_sf_airy_Ai_0[5] = {
-4.340166216535059220e+02,
-4.340166157280960419e+02,
-4.340166098026861619e+02,
-4.340166098026861619e+02,
-4.340165992684903813e+02,
};
static double array_y_sf_airy_Ai_0[5] = {
-3.051757659504586150e-05,
-1.525878852205894756e-05,
-2.165504844089681215e-13,
-2.165504844089681215e-13,
2.712707888095413635e-05,
};
static double array_e_y_sf_airy_Ai_0[5] = {
-6.103515111336886220e-05,
-3.051757659504586150e-05,
-1.525878852205894756e-05,
2.712707888095413635e-05,
6.103515521804856597e-05,
};
static double array_detla_sf_airy_Ai_0[5] = {
1.463800231600187614e-13,
1.463800309671780640e-13,
1.463800331977950112e-13,
1.463800323945595709e-13,
1.463800238025195387e-13,
};
static double array_idx_sf_airy_Ai_0[6] = {
0.000000000000000000e+00,
2.084818260000000000e+08,
3.127227390000000000e+08,
4.169636520000000000e+08,
6.022831840000000000e+08,
8.339273350000000000e+08,
};
static double array_maxE_sf_airy_Ai_0[5] = {
9.933851678693973036e-03,
4.966925646348680813e-03,
1.655642042948148214e-03,
-2.943400696150874889e-03,
-9.565968185904721519e-03,
};
double accuracy_improve_patch_of_gsl_sf_airy_Ai_0(double x)
{
 long int n = 833927336;
 int len_glob = 5;
 double ulp_x = 5.684341886080802e-14;
 double x_0 = -434.0166335043257;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_airy_Ai_0[idx])&&(n_x<array_idx_sf_airy_Ai_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_airy_Ai_0[idx+1])*(n_x-array_idx_sf_airy_Ai_0[idx])*array_maxE_sf_airy_Ai_0[idx];
         return (x-array_x_sf_airy_Ai_0[idx])/ulp_x*array_detla_sf_airy_Ai_0[idx]+array_y_sf_airy_Ai_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_airy_Ai_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_airy_Ai_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_airy_Ai_0[idx]){
         return array_y_sf_airy_Ai_0[idx];
     }
     else{
         return array_e_y_sf_airy_Ai_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_airy_Ai(double x)
{
if(x<=-434.0165861010449){
 return accuracy_improve_patch_of_gsl_sf_airy_Ai_0(x);
}
}
