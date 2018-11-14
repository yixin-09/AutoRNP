static double array_x_sf_airy_Bi_deriv_0[2] = {
-4.056502390760830394e+02,
-4.056502390760830394e+02,
};
static double array_y_sf_airy_Bi_deriv_0[2] = {
-9.159301311564776906e-13,
-9.159301311564776906e-13,
};
static double array_e_y_sf_airy_Bi_deriv_0[2] = {
1.525856841947791442e-05,
-1.422460115397984813e-05,
};
static double array_detla_sf_airy_Bi_deriv_0[2] = {
-2.898805362762331358e-12,
-2.898805360698903066e-12,
};
static double array_idx_sf_airy_Bi_deriv_0[3] = {
0.000000000000000000e+00,
5.263744000000000000e+06,
1.017080000000000000e+07,
};
static double array_maxE_sf_airy_Bi_deriv_0[2] = {
6.131011222333587751e-02,
6.430005390607791693e-02,
};
double accuracy_improve_patch_of_gsl_sf_airy_Bi_deriv_0(double x)
{
 long int n = 10170801;
 int len_glob = 2;
 double ulp_x = 5.684341886080802e-14;
 double x_0 = -405.65023937529224;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_airy_Bi_deriv_0[idx])&&(n_x<array_idx_sf_airy_Bi_deriv_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_airy_Bi_deriv_0[idx+1])*(n_x-array_idx_sf_airy_Bi_deriv_0[idx])*array_maxE_sf_airy_Bi_deriv_0[idx];
         return (x-array_x_sf_airy_Bi_deriv_0[idx])/ulp_x*array_detla_sf_airy_Bi_deriv_0[idx]+array_y_sf_airy_Bi_deriv_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_airy_Bi_deriv_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_airy_Bi_deriv_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_airy_Bi_deriv_0[idx]){
         return array_y_sf_airy_Bi_deriv_0[idx];
     }
     else{
         return array_e_y_sf_airy_Bi_deriv_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_airy_Bi_deriv(double x)
{
if(x<=-405.6502387971492){
 return accuracy_improve_patch_of_gsl_sf_airy_Bi_deriv_0(x);
}
}
