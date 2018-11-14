static double array_x_sf_airy_Ai_0[2] = {
-4.340166098026861619e+02,
-4.340166098026861619e+02,
};
static double array_y_sf_airy_Ai_0[2] = {
-2.165504844089681215e-13,
-2.165504844089681215e-13,
};
static double array_e_y_sf_airy_Ai_0[2] = {
-3.814693898674694115e-06,
3.814693465573725899e-06,
};
static double array_detla_sf_airy_Ai_0[2] = {
1.463800335463289557e-13,
1.463800335463289810e-13,
};
static double array_idx_sf_airy_Ai_0[3] = {
0.000000000000000000e+00,
2.606020500000000000e+07,
5.212041000000000000e+07,
};
static double array_maxE_sf_airy_Ai_0[2] = {
4.139106944191016748e-04,
-4.139099224245022975e-04,
};
double accuracy_improve_patch_of_gsl_sf_airy_Ai_0(double x)
{
 long int n = 52120411;
 int len_glob = 2;
 double ulp_x = 5.684341886080802e-14;
 double x_0 = -434.0166112840373;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_airy_Ai_0[idx])&&(n_x<array_idx_sf_airy_Ai_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_airy_Ai_0[idx+1])*(n_x-array_idx_sf_airy_Ai_0[idx])*array_maxE_sf_airy_Ai_0[idx];
         return (x-array_x_sf_airy_Ai_0[idx])/ulp_x*array_detla_sf_airy_Ai_0[idx]+array_y_sf_airy_Ai_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_airy_Ai_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_airy_Ai_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_airy_Ai_0[idx]){
         return array_y_sf_airy_Ai_0[idx];
     }
     else{
         return array_e_y_sf_airy_Ai_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_airy_Ai(double x)
{
if(x<=-434.016608321335){
 return accuracy_improve_patch_of_gsl_sf_airy_Ai_0(x);
}
}
