static double array_x_sf_psi_0[2] = {
-1.829873919913647342e+03,
-1.829873919913647342e+03,
};
static double array_y_sf_psi_0[2] = {
-5.743609863643113040e-12,
-5.743609863643113040e-12,
};
static double array_e_y_sf_psi_0[2] = {
-2.441381033114941245e-04,
2.441403091521629389e-04,
};
static double array_detla_sf_psi_0[2] = {
1.507605163244481847e-11,
1.507521760028908012e-11,
};
static double array_idx_sf_psi_0[3] = {
0.000000000000000000e+00,
1.619376900000000000e+07,
3.238858100000000000e+07,
};
static double array_maxE_sf_psi_0[2] = {
-4.981149538627230982e+02,
-4.980712104750206777e+02,
};
double accuracy_improve_patch_of_gsl_sf_psi_0(double x)
{
 long int n = 32388582;
 int len_glob = 2;
 double ulp_x = 2.2737367544323206e-13;
 double x_0 = -1829.8739235956841;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_psi_0[idx])&&(n_x<array_idx_sf_psi_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_psi_0[idx+1])*(n_x-array_idx_sf_psi_0[idx])*array_maxE_sf_psi_0[idx];
         return (x-array_x_sf_psi_0[idx])/ulp_x*array_detla_sf_psi_0[idx]+array_y_sf_psi_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_psi_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_psi_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_psi_0[idx]){
         return array_y_sf_psi_0[idx];
     }
     else{
         return array_e_y_sf_psi_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_psi(double x)
{
if(x<=-1829.8739162313734){
 return accuracy_improve_patch_of_gsl_sf_psi_0(x);
}
}
