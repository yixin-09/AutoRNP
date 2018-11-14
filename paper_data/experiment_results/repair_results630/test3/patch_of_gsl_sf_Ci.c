static double array_x_sf_Ci_0[2] = {
3.384180422551186229e+00,
3.384180422551186229e+00,
};
static double array_y_sf_Ci_0[2] = {
5.656852201571235655e-17,
5.656852201571235655e-17,
};
static double array_e_y_sf_Ci_0[2] = {
1.907348629534525905e-06,
-1.907348625534053881e-06,
};
static double array_detla_sf_Ci_0[2] = {
-1.273829483598037807e-16,
-1.273824884601261398e-16,
};
static double array_idx_sf_Ci_0[3] = {
0.000000000000000000e+00,
1.497334340300000000e+10,
2.994674083500000000e+10,
};
static double array_maxE_sf_Ci_0[2] = {
7.787020047269688217e-02,
7.787084811774135085e-02,
};
double accuracy_improve_patch_of_gsl_sf_Ci_0(double x)
{
 long int n = 29946740836;
 int len_glob = 2;
 double ulp_x = 4.440892098500626e-16;
 double x_0 = 3.3841737730509456;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_Ci_0[idx])&&(n_x<array_idx_sf_Ci_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_Ci_0[idx+1])*(n_x-array_idx_sf_Ci_0[idx])*array_maxE_sf_Ci_0[idx];
         return (x-array_x_sf_Ci_0[idx])/ulp_x*array_detla_sf_Ci_0[idx]+array_y_sf_Ci_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_Ci_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_Ci_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_Ci_0[idx]){
         return array_y_sf_Ci_0[idx];
     }
     else{
         return array_e_y_sf_Ci_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_Ci(double x)
{
if(x<=3.3841870720754206){
 return accuracy_improve_patch_of_gsl_sf_Ci_0(x);
}
}
