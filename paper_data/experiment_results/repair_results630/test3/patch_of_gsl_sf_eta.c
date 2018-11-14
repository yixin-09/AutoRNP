static double array_x_sf_eta_0[1] = {
-2.000000000000000000e+00,
};
static double array_y_sf_eta_0[1] = {
0.000000000000000000e+00,
};
static double array_e_y_sf_eta_0[1] = {
-4.768371383482190773e-07,
};
static double array_detla_sf_eta_0[1] = {
9.465275772057066504e-17,
};
static double array_idx_sf_eta_0[2] = {
0.000000000000000000e+00,
5.037752199000000000e+09,
};
static double array_maxE_sf_eta_0[1] = {
6.133029906205267334e-02,
};
double accuracy_improve_patch_of_gsl_sf_eta_0(double x)
{
 long int n = 5037752200;
 int len_glob = 1;
 double ulp_x = 4.440892098500626e-16;
 double x_0 = -2.0000022372113935;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_eta_0[idx])&&(n_x<array_idx_sf_eta_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_eta_0[idx+1])*(n_x-array_idx_sf_eta_0[idx])*array_maxE_sf_eta_0[idx];
         return (x-array_x_sf_eta_0[idx])/ulp_x*array_detla_sf_eta_0[idx]+array_y_sf_eta_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_eta_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_eta_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_eta_0[idx]){
         return array_y_sf_eta_0[idx];
     }
     else{
         return array_e_y_sf_eta_0[idx];
     }
 }
}
static double array_x_sf_eta_1[1] = {
-1.999999999999999778e+00,
};
static double array_y_sf_eta_1[1] = {
4.732640932675400909e-17,
};
static double array_e_y_sf_eta_1[1] = {
4.768371577152526042e-07,
};
static double array_detla_sf_eta_1[1] = {
4.732643979312525517e-17,
};
static double array_idx_sf_eta_1[2] = {
0.000000000000000000e+00,
1.007549183400000000e+10,
};
static double array_maxE_sf_eta_1[1] = {
6.133011960055805012e-02,
};
double accuracy_improve_patch_of_gsl_sf_eta_1(double x)
{
 long int n = 10075491835;
 int len_glob = 1;
 double ulp_x = 2.220446049250313e-16;
 double x_0 = -1.9999999999999998;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_eta_1[idx])&&(n_x<array_idx_sf_eta_1[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_eta_1[idx+1])*(n_x-array_idx_sf_eta_1[idx])*array_maxE_sf_eta_1[idx];
         return (x-array_x_sf_eta_1[idx])/ulp_x*array_detla_sf_eta_1[idx]+array_y_sf_eta_1[idx]+compen;
     }
     else if(n_x<array_idx_sf_eta_1[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_eta_1[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_eta_1[idx]){
         return array_y_sf_eta_1[idx];
     }
     else{
         return array_e_y_sf_eta_1[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_eta(double x)
{
if(x<=-2.0){
 return accuracy_improve_patch_of_gsl_sf_eta_0(x);
}
if(x<=-1.999997762791396){
 return accuracy_improve_patch_of_gsl_sf_eta_1(x);
}
}
