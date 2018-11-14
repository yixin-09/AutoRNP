static double array_x_sf_clausen_0[2] = {
-7.853981633974483145e+01,
-7.853981633974483145e+01,
};
static double array_y_sf_clausen_0[2] = {
3.404022797704446351e-16,
3.404022797704446351e-16,
};
static double array_e_y_sf_clausen_0[2] = {
1.995042451549009804e-06,
-1.907348114497892508e-06,
};
static double array_detla_sf_clausen_0[2] = {
-9.850213879184367981e-15,
-9.850213879184789233e-15,
};
static double array_idx_sf_clausen_0[3] = {
0.000000000000000000e+00,
2.025379830000000000e+08,
3.961731810000000000e+08,
};
static double array_maxE_sf_clausen_0[2] = {
-1.799532154091814295e-07,
1.720472091688599843e-07,
};
double accuracy_improve_patch_of_gsl_sf_clausen_0(double x)
{
 long int n = 396173182;
 int len_glob = 2;
 double ulp_x = 1.4210854715202004e-14;
 double x_0 = -78.53981921798268;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_clausen_0[idx])&&(n_x<array_idx_sf_clausen_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_clausen_0[idx+1])*(n_x-array_idx_sf_clausen_0[idx])*array_maxE_sf_clausen_0[idx];
         return (x-array_x_sf_clausen_0[idx])/ulp_x*array_detla_sf_clausen_0[idx]+array_y_sf_clausen_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_clausen_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_clausen_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_clausen_0[idx]){
         return array_y_sf_clausen_0[idx];
     }
     else{
         return array_e_y_sf_clausen_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_clausen(double x)
{
if(x<=-78.53981358802316){
 return accuracy_improve_patch_of_gsl_sf_clausen_0(x);
}
}
