static double array_x_sf_legendre_P2_0[5] = {
-5.776321096981537062e-01,
-5.774100650932286749e-01,
-5.773502691896258421e-01,
-5.773502691896258421e-01,
-5.772990427907661592e-01,
};
static double array_y_sf_legendre_P2_0[5] = {
4.882812315098154104e-04,
1.035749064498632163e-04,
1.343586828703485937e-16,
1.343586828703485937e-16,
-8.872278929771451714e-05,
};
static double array_e_y_sf_legendre_P2_0[5] = {
2.959095800523731741e-04,
2.959095800523731741e-04,
1.035749064498632163e-04,
-8.872278929771451714e-05,
-2.441406249789577500e-04,
};
static double array_detla_sf_legendre_P2_0[5] = {
-1.923716514574422474e-16,
-1.923346736025099632e-16,
-1.923062266567001260e-16,
-1.922877377292340085e-16,
-1.922642611974932842e-16,
};
static double array_idx_sf_legendre_P2_0[6] = {
0.000000000000000000e+00,
1.000000000000000000e+12,
2.000000000000000000e+12,
2.538593618368000000e+12,
3.000000000000000000e+12,
3.808355305938000000e+12,
};
static double array_maxE_sf_legendre_P2_0[5] = {
1.499999999996270095e+00,
1.499999999987474020e+00,
1.499999999996603828e+00,
1.500000000004808598e+00,
1.499999999991905364e+00,
};
double accuracy_improve_patch_of_gsl_sf_legendre_P2_0(double x)
{
 long int n = 3808355305939;
 int len_glob = 5;
 double ulp_x = 1.1102230246251565e-16;
 double x_0 = -0.5776321096981537;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_legendre_P2_0[idx])&&(n_x<array_idx_sf_legendre_P2_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_legendre_P2_0[idx+1])*(n_x-array_idx_sf_legendre_P2_0[idx])*array_maxE_sf_legendre_P2_0[idx];
         return (x-array_x_sf_legendre_P2_0[idx])/ulp_x*array_detla_sf_legendre_P2_0[idx]+array_y_sf_legendre_P2_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_legendre_P2_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_legendre_P2_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_legendre_P2_0[idx]){
         return array_y_sf_legendre_P2_0[idx];
     }
     else{
         return array_e_y_sf_legendre_P2_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_legendre_P2(double x)
{
if(x<=-0.5772092973234931){
 return accuracy_improve_patch_of_gsl_sf_legendre_P2_0(x);
}
}
