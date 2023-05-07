from numpy import *
from matplotlib.pyplot import *
import pandas as pd

df=pd.read_csv('SFO38_GaiaEDR3AndGaiaDistEDR3_10arcmin.csv')

print(df.keys())

#Index(['angDist', 'ra_epoch2000', 'dec_epoch2000', 'errHalfMaj', 'errHalfMin', 'errPosAng', 'source_id', 'ra', 'ra_error', 'dec', 'dec_error', 'parallax', 'parallax_error', 'parallax_over_error', 'pm', 'pmra','pmra_error', 'pmdec', 'pmdec_error', 'astrometric_n_good_obs_al', 'astrometric_gof_al', 'astrometric_chi2_al', 'astrometric_excess_noise', 'astrometric_excess_noise_sig', 'astrometric_params_solved', 'pseudocolour', 'pseudocolour_error', 'visibility_periods_used', 'ruwe', 'duplicated_source', 'phot_g_mean_flux', 'phot_g_mean_flux_error', 'phot_g_mean_mag', 'phot_bp_mean_flux', 'phot_bp_mean_flux_error', 'phot_bp_mean_mag', 'phot_rp_mean_flux', 'phot_rp_mean_mag', 'phot_bp_rp_excess_factor', 'bp_rp', 'dr2_radial_velocity', 'dr2_radial_velocity_error', 'dr2_rv_nb_transits', 'dr2_rv_template_teff', 'dr2_rv_template_logg', 'panstarrs1', 'sdssdr13', 'skymapper2', 'urat1', 'phot_g_mean_mag_error', 'phot_bp_mean_mag_error', 'phot_rp_mean_mag_error', 'phot_g_mean_mag_corrected', 'phot_g_mean_mag_error_corrected', 'phot_g_mean_flux_corrected', 'phot_bp_rp_excess_factor_corrected', 'ra_epoch2000_error', 'dec_epoch2000_error', 'ra_dec_epoch2000_corr', 'Source', 'RA_ICRS', 'DE_ICRS', 'rgeo', 'b_rgeo', 'B_rgeo', 'rpgeo','b_rpgeo', 'B_rpgeo', 'Flag'], dtype='object')


dist=df['angDist'].tolist()
ra=df['ra'].tolist()
ra_error=df['ra_error'].tolist()
dec=df['dec'].tolist()
dec_error=df['dec_error'].tolist()
source_id=df['source_id'].tolist()
pmra=df['pmra'].tolist()
pmra_error=df['pmra_error'].tolist()
pmde=df['pmdec'].tolist()
pmde_error=df['pmdec_error'].tolist()
brgeo=df['b_rgeo'].tolist()
Brgeo=df['B_rgeo'].tolist()

dist_new=[]
ra_new=[]
ra_error_new=[]
dec_new=[]
dec_error_new=[]
source_id_new=[]
pmra_new=[]
pmra_error_new=[]
pmde_new=[]
pmde_error_new=[]
brgeo_new=[]
Brgeo_new=[]

for (i,j,k,l,m,n,o,p,q,r,s,t) in zip(dist, ra, ra_error, dec, dec_error, source_id, pmra, pmra_error, pmde, pmde_error, brgeo, Brgeo):
        delD=(s+t)/2
        if (q/r)>3 and (o/p)>3 and (i/delD)>3:
        	dist_new.append(i)
        	ra_new.append(j)
        	ra_error_new.append(k)
        	dec_new.append(l)
        	dec_error_new.append(m)
        	source_id_new.append(n)
        	pmra_new.append(o)
        	pmra_error_new.append(p)
        	pmde_new.append(q)
        	pmde_error_new.append(r)
        	brgeo_new.append(s)
        	Brgeo_new.append(t)

dict={'source_id': source_id_new, 'ra': ra_new, 'ra_error': ra_error_new, 'dec': dec_new, 'dec_error': dec_error_new, 'angDist': dist_new, 'pmra': pmra_new, 'pmra_error': pmra_error_new, 'pmde': pmde_new, 'pmde_error': pmde_error_new, 'b_rgeo': brgeo_new, "B_rgeo": Brgeo_new}
df1 = pd.DataFrame(dict) 
    
# saving the dataframe 
df1.to_csv('New_SFO38_before_MAD.csv')

scatter(pmra_new, dist_new)
xlabel('Ang Dist(pc)')
ylabel('pmra')
savefig('pmra_dist.png')
clf()
scatter(pmde_new, dist_new)
xlabel('Ang Dist(pc)')
ylabel('pmde')
savefig('pmde_dist.png')
