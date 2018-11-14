static double array_x_sf_bessel_Y1_0[4] = {
3.061827987653054350e+01,
3.061828649164111482e+01,
3.061828649164111482e+01,
3.061829310675443594e+01,
};
static double array_y_sf_bessel_Y1_0[4] = {
9.536741654961758698e-07,
-1.524456280251315065e-17,
-1.524456280251315065e-17,
-9.536743559121065820e-07,
};
static double array_e_y_sf_bessel_Y1_0[4] = {
1.907348537008205979e-06,
9.536741654961758698e-07,
-9.536743559121065820e-07,
-1.907348505724989707e-06,
};
static double array_detla_sf_bessel_Y1_0[4] = {
-5.121807032951038951e-16,
-5.121805926603419585e-16,
-5.121804820032158153e-16,
-5.121803713237253667e-16,
};
static double array_idx_sf_bessel_Y1_0[5] = {
0.000000000000000000e+00,
1.861988094000000000e+09,
3.723976188000000000e+09,
5.585965056000000000e+09,
7.447953924000000000e+09,
};
static double array_maxE_sf_bessel_Y1_0[4] = {
2.353533814535168148e-03,
2.354009131934921978e-03,
2.354484437212777271e-03,
2.354959744539141930e-03,
};
double accuracy_improve_patch_of_gsl_sf_bessel_Y1_0(double x)
{
 long int n = 7447953925;
 int len_glob = 4;
 double ulp_x = 3.552713678800501e-15;
 double x_0 = 30.618273261419972;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_bessel_Y1_0[idx])&&(n_x<array_idx_sf_bessel_Y1_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_bessel_Y1_0[idx+1])*(n_x-array_idx_sf_bessel_Y1_0[idx])*array_maxE_sf_bessel_Y1_0[idx];
         return (x-array_x_sf_bessel_Y1_0[idx])/ulp_x*array_detla_sf_bessel_Y1_0[idx]+array_y_sf_bessel_Y1_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_bessel_Y1_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_bessel_Y1_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_bessel_Y1_0[idx]){
         return array_y_sf_bessel_Y1_0[idx];
     }
     else{
         return array_e_y_sf_bessel_Y1_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_bessel_Y1(double x)
{
if(x<=30.618299721867757){
 return accuracy_improve_patch_of_gsl_sf_bessel_Y1_0(x);
}
}
