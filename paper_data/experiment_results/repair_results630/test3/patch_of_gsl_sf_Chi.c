static double array_x_sf_Chi_0[6] = {
5.238190668599789213e-01,
5.238208191249216217e-01,
5.238225713898643221e-01,
5.238225713898643221e-01,
5.238243236723481022e-01,
5.238260759548318823e-01,
};
static double array_y_sf_Chi_0[6] = {
-7.629375431561137819e-06,
-3.814682941893502377e-06,
-1.836318268327936040e-16,
-1.836318268327936040e-16,
3.814711580452839224e-06,
7.629413613091570509e-06,
};
static double array_e_y_sf_Chi_0[6] = {
-1.525878905531376909e-05,
-7.629375431561137819e-06,
-3.814682941893502377e-06,
3.814711580452839224e-06,
7.629413613091570509e-06,
1.525878903443648725e-05,
};
static double array_detla_sf_Chi_0[6] = {
2.416972017986332096e-16,
2.416962943609916442e-16,
2.416956894089498123e-16,
2.416950844586694575e-16,
2.416944795101507277e-16,
2.416935720969514259e-16,
};
static double array_idx_sf_Chi_0[7] = {
0.000000000000000000e+00,
3.156599897300000000e+10,
4.734899845900000000e+10,
6.313199794500000000e+10,
7.891515542700000000e+10,
9.469831290900000000e+10,
1.262646278720000000e+11,
};
static double array_maxE_sf_Chi_0[6] = {
-1.554847593755969370e+00,
-1.554829130033356321e+00,
-1.554816819715800991e+00,
-1.554804509901662968e+00,
-1.554792201485742043e+00,
-1.554773736477609747e+00,
};
double accuracy_improve_patch_of_gsl_sf_Chi_0(double x)
{
 long int n = 126264627873;
 int len_glob = 6;
 double ulp_x = 1.1102230246251565e-16;
 double x_0 = 0.5238155623300934;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_Chi_0[idx])&&(n_x<array_idx_sf_Chi_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_Chi_0[idx+1])*(n_x-array_idx_sf_Chi_0[idx])*array_maxE_sf_Chi_0[idx];
         return (x-array_x_sf_Chi_0[idx])/ulp_x*array_detla_sf_Chi_0[idx]+array_y_sf_Chi_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_Chi_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_Chi_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_Chi_0[idx]){
         return array_y_sf_Chi_0[idx];
     }
     else{
         return array_e_y_sf_Chi_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_Chi(double x)
{
if(x<=0.5238295805197993){
 return accuracy_improve_patch_of_gsl_sf_Chi_0(x);
}
}
