static double array_x_sf_zeta_0[2] = {
-4.000000000000005329e+00,
-4.000000000000000000e+00,
};
static double array_y_sf_zeta_0[2] = {
-4.254629422250002686e-17,
0.000000000000000000e+00,
};
static double array_e_y_sf_zeta_0[2] = {
-9.218363748208319328e-17,
-4.254629422250002686e-17,
};
static double array_detla_sf_zeta_0[2] = {
7.091049037083309049e-18,
7.091049037083338323e-18,
};
static double array_idx_sf_zeta_0[3] = {
0.000000000000000000e+00,
7.000000000000000000e+00,
1.300000000000000000e+01,
};
static double array_maxE_sf_zeta_0[2] = {
2.604166666666666522e-03,
2.604166666666666522e-03,
};
double accuracy_improve_patch_of_gsl_sf_zeta_0(double x)
{
 long int n = 14;
 int len_glob = 2;
 double ulp_x = 8.881784197001252e-16;
 double x_0 = -4.0000000000000115;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_zeta_0[idx])&&(n_x<array_idx_sf_zeta_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_zeta_0[idx+1])*(n_x-array_idx_sf_zeta_0[idx])*array_maxE_sf_zeta_0[idx];
         return (x-array_x_sf_zeta_0[idx])/ulp_x*array_detla_sf_zeta_0[idx]+array_y_sf_zeta_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_zeta_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_zeta_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_zeta_0[idx]){
         return array_y_sf_zeta_0[idx];
     }
     else{
         return array_e_y_sf_zeta_0[idx];
     }
 }
}
static double array_x_sf_zeta_1[1] = {
-3.999999999999999556e+00,
};
static double array_y_sf_zeta_1[1] = {
3.545524518541676095e-18,
};
static double array_e_y_sf_zeta_1[1] = {
1.192092895447024122e-07,
};
static double array_detla_sf_zeta_1[1] = {
3.545543540270764187e-18,
};
static double array_idx_sf_zeta_1[2] = {
0.000000000000000000e+00,
3.362228899100000000e+10,
};
static double array_maxE_sf_zeta_1[1] = {
2.868667697825183147e-03,
};
double accuracy_improve_patch_of_gsl_sf_zeta_1(double x)
{
 long int n = 33622288992;
 int len_glob = 1;
 double ulp_x = 4.440892098500626e-16;
 double x_0 = -3.9999999999999996;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_zeta_1[idx])&&(n_x<array_idx_sf_zeta_1[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_zeta_1[idx+1])*(n_x-array_idx_sf_zeta_1[idx])*array_maxE_sf_zeta_1[idx];
         return (x-array_x_sf_zeta_1[idx])/ulp_x*array_detla_sf_zeta_1[idx]+array_y_sf_zeta_1[idx]+compen;
     }
     else if(n_x<array_idx_sf_zeta_1[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_zeta_1[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_zeta_1[idx]){
         return array_y_sf_zeta_1[idx];
     }
     else{
         return array_e_y_sf_zeta_1[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_zeta(double x)
{
if(x<=-4.0){
 return accuracy_improve_patch_of_gsl_sf_zeta_0(x);
}
if(x<=-3.999985068704248){
 return accuracy_improve_patch_of_gsl_sf_zeta_1(x);
}
}
