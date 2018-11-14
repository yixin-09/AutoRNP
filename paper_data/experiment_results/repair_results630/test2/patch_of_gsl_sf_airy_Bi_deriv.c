static double array_x_sf_airy_Bi_deriv_0[2] = {
-4.056502390760830394e+02,
-4.056502390760830394e+02,
};
static double array_y_sf_airy_Bi_deriv_0[2] = {
-9.159301311564776906e-13,
-9.159301311564776906e-13,
};
static double array_e_y_sf_airy_Bi_deriv_0[2] = {
2.441404082648857964e-04,
-2.420080924071370005e-04,
};
static double array_detla_sf_airy_Bi_deriv_0[2] = {
-2.898805374324576738e-12,
-2.898805340340911403e-12,
};
static double array_idx_sf_airy_Bi_deriv_0[3] = {
0.000000000000000000e+00,
8.422104200000000000e+07,
1.677065000000000000e+08,
};
static double array_maxE_sf_airy_Bi_deriv_0[2] = {
3.809859607675563503e-02,
8.740016503813735627e-02,
};
double accuracy_improve_patch_of_gsl_sf_airy_Bi_deriv_0(double x)
{
 long int n = 167706501;
 int len_glob = 2;
 double ulp_x = 5.684341886080802e-14;
 double x_0 = -405.650243863495;
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
if(x<=-405.6502343304842){
 return accuracy_improve_patch_of_gsl_sf_airy_Bi_deriv_0(x);
}
}
