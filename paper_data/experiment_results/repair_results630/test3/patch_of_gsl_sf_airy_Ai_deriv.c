static double array_x_sf_airy_Ai_deriv_0[2] = {
-3.244642927988942915e+02,
-3.244642927988942915e+02,
};
static double array_y_sf_airy_Ai_deriv_0[2] = {
-2.447926953186563774e-12,
-2.447926953186563774e-12,
};
static double array_e_y_sf_airy_Ai_deriv_0[2] = {
1.525867189740326490e-05,
-1.525877729935442426e-05,
};
static double array_detla_sf_airy_Ai_deriv_0[2] = {
-2.451774002210037219e-12,
-2.451773999536836260e-12,
};
static double array_idx_sf_airy_Ai_deriv_0[3] = {
0.000000000000000000e+00,
6.223524000000000000e+06,
1.244708900000000000e+07,
};
static double array_maxE_sf_airy_Ai_deriv_0[2] = {
6.522887182295351860e-02,
6.770432164276124487e-02,
};
double accuracy_improve_patch_of_gsl_sf_airy_Ai_deriv_0(double x)
{
 long int n = 12447090;
 int len_glob = 2;
 double ulp_x = 5.684341886080802e-14;
 double x_0 = -324.4642931526607;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_airy_Ai_deriv_0[idx])&&(n_x<array_idx_sf_airy_Ai_deriv_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_airy_Ai_deriv_0[idx+1])*(n_x-array_idx_sf_airy_Ai_deriv_0[idx])*array_maxE_sf_airy_Ai_deriv_0[idx];
         return (x-array_x_sf_airy_Ai_deriv_0[idx])/ulp_x*array_detla_sf_airy_Ai_deriv_0[idx]+array_y_sf_airy_Ai_deriv_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_airy_Ai_deriv_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_airy_Ai_deriv_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_airy_Ai_deriv_0[idx]){
         return array_y_sf_airy_Ai_deriv_0[idx];
     }
     else{
         return array_e_y_sf_airy_Ai_deriv_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_airy_Ai_deriv(double x)
{
if(x<=-324.4642924451256){
 return accuracy_improve_patch_of_gsl_sf_airy_Ai_deriv_0(x);
}
}
