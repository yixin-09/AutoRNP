static double array_x_sf_legendre_P3_0[2] = {
7.745966692414834043e-01,
7.745966692414834043e-01,
};
static double array_y_sf_legendre_P3_0[2] = {
8.172618520478209880e-17,
8.172618520478209880e-17,
};
static double array_e_y_sf_legendre_P3_0[2] = {
-1.907348621772972426e-06,
1.556349585409543408e-06,
};
static double array_detla_sf_legendre_P3_0[2] = {
3.330664973190943705e-16,
3.330672419927413951e-16,
};
static double array_idx_sf_legendre_P3_0[3] = {
0.000000000000000000e+00,
5.726630079000000000e+09,
1.039940899300000000e+10,
};
static double array_maxE_sf_legendre_P3_0[2] = {
5.809472636447479132e+00,
5.809476965823981764e+00,
};
double accuracy_improve_patch_of_gsl_sf_legendre_P3_0(double x)
{
 long int n = 10399408994;
 int len_glob = 2;
 double ulp_x = 1.1102230246251565e-16;
 double x_0 = 0.7745960334578267;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_legendre_P3_0[idx])&&(n_x<array_idx_sf_legendre_P3_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_legendre_P3_0[idx+1])*(n_x-array_idx_sf_legendre_P3_0[idx])*array_maxE_sf_legendre_P3_0[idx];
         return (x-array_x_sf_legendre_P3_0[idx])/ulp_x*array_detla_sf_legendre_P3_0[idx]+array_y_sf_legendre_P3_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_legendre_P3_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_legendre_P3_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_legendre_P3_0[idx]){
         return array_y_sf_legendre_P3_0[idx];
     }
     else{
         return array_e_y_sf_legendre_P3_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_legendre_P3(double x)
{
if(x<=0.7745971880241573){
 return accuracy_improve_patch_of_gsl_sf_legendre_P3_0(x);
}
}
