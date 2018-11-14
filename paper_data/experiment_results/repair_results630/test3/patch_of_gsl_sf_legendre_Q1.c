static double array_x_sf_legendre_Q1_0[6] = {
8.335526779143836995e-01,
8.335555891793193783e-01,
8.335565596009646416e-01,
8.335565596009646416e-01,
8.335575300026489831e-01,
8.335585004043333246e-01,
};
static double array_y_sf_legendre_Q1_0[6] = {
-1.525877935353949337e-05,
-3.814725171464131723e-06,
-2.232976000570467603e-16,
-2.232976000570467603e-16,
3.814666926283414013e-06,
7.629354074398386928e-06,
};
static double array_e_y_sf_legendre_Q1_0[6] = {
-7.629430120693582928e-06,
-7.629430120693582928e-06,
-3.814725171464131723e-06,
3.814666926283414013e-06,
7.629354074398386928e-06,
1.525878903674712367e-05,
};
static double array_detla_sf_legendre_Q1_0[6] = {
4.364226222199654433e-16,
4.364260924576785860e-16,
4.364284059821914995e-16,
4.364307195074384480e-16,
4.364330330334193330e-16,
4.364365033714474304e-16,
};
static double array_idx_sf_legendre_Q1_0[7] = {
0.000000000000000000e+00,
1.748156223900000000e+10,
2.622234335900000000e+10,
3.496312447900000000e+10,
4.370372580700000000e+10,
5.244432713500000000e+10,
6.992552979200000000e+10,
};
static double array_maxE_sf_legendre_Q1_0[6] = {
1.073653628679826433e+01,
1.073670703267634430e+01,
1.073682086048279594e+01,
1.073693469604312511e+01,
1.073704852943193622e+01,
1.073721928413342042e+01,
};
double accuracy_improve_patch_of_gsl_sf_legendre_Q1_0(double x)
{
 long int n = 69925529793;
 int len_glob = 6;
 double ulp_x = 1.1102230246251565e-16;
 double x_0 = 0.8335526779143837;
 double compen = 0.0;
 double n_x = ((x-x_0)/ulp_x);
 int idx = floor(n_x*len_glob/n);
 while((idx>=0)&&(idx<len_glob)){
     if((n_x>array_idx_sf_legendre_Q1_0[idx])&&(n_x<array_idx_sf_legendre_Q1_0[idx+1])){
         compen = ulp_x*ulp_x * (n_x-array_idx_sf_legendre_Q1_0[idx+1])*(n_x-array_idx_sf_legendre_Q1_0[idx])*array_maxE_sf_legendre_Q1_0[idx];
         return (x-array_x_sf_legendre_Q1_0[idx])/ulp_x*array_detla_sf_legendre_Q1_0[idx]+array_y_sf_legendre_Q1_0[idx]+compen;
     }
     else if(n_x<array_idx_sf_legendre_Q1_0[idx]){
         idx = idx - 1;
     }
     else if(n_x>array_idx_sf_legendre_Q1_0[idx+1]){
         idx = idx + 1;
     }
     else if(x==array_x_sf_legendre_Q1_0[idx]){
         return array_y_sf_legendre_Q1_0[idx];
     }
     else{
         return array_e_y_sf_legendre_Q1_0[idx];
     }
 }
}
double accuracy_improve_patch_of_gsl_sf_legendre_Q1(double x)
{
if(x<=0.8335604412077021){
 return accuracy_improve_patch_of_gsl_sf_legendre_Q1_0(x);
}
}
