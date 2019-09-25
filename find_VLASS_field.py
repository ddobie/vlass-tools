from astropy.table import Table
from astropy.io import ascii
from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np

def load_vlass(vlass_table = 'vlass_fields.dat'):
  table_cols = ['tile_name', 'dec_min', 'dec_max', 'ra_min', 'ra_max', 'obs_epoch', 'obs_date', 'imaging_status']

  vlass_fields = Table.read(vlass_table, format='ascii', data_start=3)
  vlass_fields.remove_column('col9')
  
  vlass_fields.rename_columns(vlass_fields.colnames, table_cols)
  
  vlass_fields['dec_min'] *= u.deg
  vlass_fields['dec_max'] *= u.deg
  vlass_fields['ra_min'] *= u.hourangle
  vlass_fields['ra_max'] *= u.hourangle

  return vlass_fields



def search_fields(coord, vlass_fields):
  dec_mins = np.asarray(vlass_fields['dec_min'])
  dec_maxs = np.asarray(vlass_fields['dec_max'])
  coord_dec = coord.dec.deg
  coord_ra = coord.ra.hour
  
  dec_id_min = np.searchsorted(dec_maxs, coord_dec)
  dec_id_max = np.searchsorted(dec_mins, coord_dec)
  if dec_id_min > dec_id_max:
    temp = dec_id_min
    dec_id_min = dec_id_max
    dec_id_max = temp
    
  fields_cut = vlass_fields[dec_id_min:dec_id_max]
  
  ra_mins = np.asarray(fields_cut['ra_min'])
  ra_maxs = np.asarray(fields_cut['ra_max'])
  
  ra_id_min = np.searchsorted(ra_maxs, coord_ra)
  ra_id_max = np.searchsorted(ra_mins, coord_ra)
  
  print(fields_cut[ra_id_min:ra_id_max])
  
  #for i, row in enumerate(fields_cut):
  #  print(i, row['ra_min'], row['ra_max'])
  
if __name__ == '__main__':
  vlass_fields = load_vlass()

  coord = SkyCoord(14.429, -27.013, unit=u.deg)
  
  coord = SkyCoord("00h57m42.9s -27d00m46.5s")
  
  coord = SkyCoord(14.504, -23.914, unit=u.deg)
  
  coord = SkyCoord(13.948, -27.076, unit=u.deg)

  search_fields(coord, vlass_fields)

  print(coord)
  print(coord.to_string('hmsdms',sep=':'))
