static double array_x_sf_lnsinh_0[2] = {
8.813735870195430477e-01,
8.813735870195430477e-01,
};
static double array_y_sf_lnsinh_0[2] = {
3.182752524377401230e-17,
3.182752524377401230e-17,
};
static double array_e_y_sf_lnsinh_0[2] = {
-1.907348612010903522e-06,
3.814352171883111144e-06,
};
static double array_detla_sf_lnsinh_0[2] = {
1.570093207362788003e-16,
1.570090961464759605e-16,
};
static double array_idx_sf_lnsinh_0[3] = {
0.000000000000000000e+00,
1.214799607500000000e+10,
3.644182532100000000e+10,
};
static double array_maxE_sf_lnsinh_0[2] = {
-5.000009536215692663e-01,
-4.999980929119131057e-01,
};
double accuracy_improve_patch_of_gsl_sf_lnsinh_0(double x)
{
 long int n = 36441825322;
 int len_glob = 2;
 double ulp_x = 1.1102230246251565e-16;
 double x_0 = 0.8813722383210485;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_lnsinh_0[idx])&&(n_x<array_idx_sf_lnsinh_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_lnsinh_0[idx+1])*(n_x-array_idx_sf_lnsinh_0[idx])*array_maxE_sf_lnsinh_0[idx];
         return (x-array_x_sf_lnsinh_0[idx])/ulp_x*array_detla_sf_lnsinh_0[idx]+array_y_sf_lnsinh_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_lnsinh_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_lnsinh_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_lnsinh_0[idx]){
         return array_y_sf_lnsinh_0[idx];
     }
     else{
         return array_e_y_sf_lnsinh_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_lnsinh(double x)
{
if(x<=0.8813762841764016){
 return accuracy_improve_patch_of_gsl_sf_lnsinh_0(x);
}
}
