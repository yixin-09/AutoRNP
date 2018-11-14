static double array_x_sf_bessel_J1_0[2] = {
3.831705970207512024e+00,
3.831705970207512024e+00,
};
static double array_y_sf_bessel_J1_0[2] = {
1.173630282272863872e-16,
1.173630282272863872e-16,
};
static double array_e_y_sf_bessel_J1_0[2] = {
9.536743327563988671e-07,
-9.536743021275018883e-07,
};
static double array_detla_sf_bessel_J1_0[2] = {
-1.788611570618270377e-16,
-1.788610465323455161e-16,
};
static double array_idx_sf_bessel_J1_0[3] = {
0.000000000000000000e+00,
5.331925323000000000e+09,
1.066385377100000000e+10,
};
static double array_maxE_sf_bessel_J1_0[2] = {
5.255595614024471257e-02,
5.255633563486650922e-02,
};
double accuracy_improve_patch_of_gsl_sf_bessel_J1_0(double x)
{
 long int n = 10663853772;
 int len_glob = 2;
 double ulp_x = 4.440892098500626e-16;
 double x_0 = 3.8317036023570084;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_bessel_J1_0[idx])&&(n_x<array_idx_sf_bessel_J1_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_bessel_J1_0[idx+1])*(n_x-array_idx_sf_bessel_J1_0[idx])*array_maxE_sf_bessel_J1_0[idx];
         return (x-array_x_sf_bessel_J1_0[idx])/ulp_x*array_detla_sf_bessel_J1_0[idx]+array_y_sf_bessel_J1_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_bessel_J1_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_bessel_J1_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_bessel_J1_0[idx]){
         return array_y_sf_bessel_J1_0[idx];
     }
     else{
         return array_e_y_sf_bessel_J1_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_bessel_J1(double x)
{
if(x<=3.8317083380594035){
 return accuracy_improve_patch_of_gsl_sf_bessel_J1_0(x);
}
}
