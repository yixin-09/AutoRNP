static double array_x_sf_bessel_J0_0[2] = {
2.002771557933324118e+02,
2.002771557933324118e+02,
};
static double array_y_sf_bessel_J0_0[2] = {
1.159668494172413755e-18,
1.159668494172413755e-18,
};
static double array_e_y_sf_bessel_J0_0[2] = {
-1.192092054417068715e-07,
1.192092170048239439e-07,
};
static double array_detla_sf_bessel_J0_0[2] = {
1.602415834975132219e-15,
1.602415818057927868e-15,
};
static double array_idx_sf_bessel_J0_0[3] = {
0.000000000000000000e+00,
7.439342700000000000e+07,
1.487868620000000000e+08,
};
static double array_maxE_sf_bessel_J0_0[2] = {
-1.407251339364202689e-04,
-1.407847320909741049e-04,
};
double accuracy_improve_patch_of_gsl_sf_bessel_J0_0(double x)
{
 long int n = 148786863;
 int len_glob = 2;
 double ulp_x = 2.842170943040401e-14;
 double x_0 = 200.27715367894405;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_bessel_J0_0[idx])&&(n_x<array_idx_sf_bessel_J0_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_bessel_J0_0[idx+1])*(n_x-array_idx_sf_bessel_J0_0[idx])*array_maxE_sf_bessel_J0_0[idx];
         return (x-array_x_sf_bessel_J0_0[idx])/ulp_x*array_detla_sf_bessel_J0_0[idx]+array_y_sf_bessel_J0_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_bessel_J0_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_bessel_J0_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_bessel_J0_0[idx]){
         return array_y_sf_bessel_J0_0[idx];
     }
     else{
         return array_e_y_sf_bessel_J0_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_bessel_J0(double x)
{
if(x<=200.277157907721){
 return accuracy_improve_patch_of_gsl_sf_bessel_J0_0(x);
}
}
