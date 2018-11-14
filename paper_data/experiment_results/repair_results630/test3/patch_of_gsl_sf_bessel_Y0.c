static double array_x_sf_bessel_Y0_0[2] = {
3.957678419314857976e+00,
3.957678419314857976e+00,
};
static double array_y_sf_bessel_Y0_0[2] = {
-4.333106464293519434e-17,
-4.333106464293519434e-17,
};
static double array_e_y_sf_bessel_Y0_0[2] = {
1.907348614242858419e-06,
-1.907348623095975633e-06,
};
static double array_detla_sf_bessel_Y0_0[2] = {
-1.787649640501956813e-16,
-1.787647500275159146e-16,
};
static double array_idx_sf_bessel_Y0_0[3] = {
0.000000000000000000e+00,
1.066958855400000000e+10,
2.133918993100000000e+10,
};
static double array_maxE_sf_bessel_Y0_0[2] = {
5.085549362987843575e-02,
5.085632555038593905e-02,
};
double accuracy_improve_patch_of_gsl_sf_bessel_Y0_0(double x)
{
 long int n = 21339189932;
 int len_glob = 2;
 double ulp_x = 4.440892098500626e-16;
 double x_0 = 3.9576736810657076;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_bessel_Y0_0[idx])&&(n_x<array_idx_sf_bessel_Y0_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_bessel_Y0_0[idx+1])*(n_x-array_idx_sf_bessel_Y0_0[idx])*array_maxE_sf_bessel_Y0_0[idx];
         return (x-array_x_sf_bessel_Y0_0[idx])/ulp_x*array_detla_sf_bessel_Y0_0[idx]+array_y_sf_bessel_Y0_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_bessel_Y0_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_bessel_Y0_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_bessel_Y0_0[idx]){
         return array_y_sf_bessel_Y0_0[idx];
     }
     else{
         return array_e_y_sf_bessel_Y0_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_bessel_Y0(double x)
{
if(x<=3.957683157569703){
 return accuracy_improve_patch_of_gsl_sf_bessel_Y0_0(x);
}
}
