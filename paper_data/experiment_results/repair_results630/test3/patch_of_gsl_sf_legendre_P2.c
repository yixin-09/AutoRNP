static double array_x_sf_legendre_P2_0[2] = {
-5.773502691896258421e-01,
-5.773502691896258421e-01,
};
static double array_y_sf_legendre_P2_0[2] = {
1.343586828703485937e-16,
1.343586828703485937e-16,
};
static double array_e_y_sf_legendre_P2_0[2] = {
1.524500715235502819e-05,
-7.629394525699947056e-06,
};
static double array_detla_sf_legendre_P2_0[2] = {
-1.922977344061790642e-16,
-1.922955350835084744e-16,
};
static double array_idx_sf_legendre_P2_0[3] = {
0.000000000000000000e+00,
7.927814230000000000e+10,
1.189535020140000000e+11,
};
static double array_maxE_sf_legendre_P2_0[2] = {
1.500000000058489436e+00,
1.499999999924946703e+00,
};
double accuracy_improve_patch_of_gsl_sf_legendre_P2_0(double x)
{
 long int n = 118953502015;
 int len_glob = 2;
 double ulp_x = 1.1102230246251565e-16;
 double x_0 = -0.5773590708315189;
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
if(x<=-0.5773458643398394){
 return accuracy_improve_patch_of_gsl_sf_legendre_P2_0(x);
}
}
