from astropy.table import Table
from astropy.io import ascii
from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np

def load_image_list(vlass_list = 'vlass_imagelist.csv'):
    vlass_images = Table.read(vlass_list, format='csv')
    
    vlass_images['RA'] *= u.deg
    vlass_images['Dec'] *= u.deg
    
    return vlass_images
    
def find_image(vlass_coords, coord):
    seps = vlass_coords.separation(coord)
    index = np.argmin(seps)
    
    return index
  
if __name__ == '__main__':
    vlass_fields = load_image_list()
    vlass_coords = SkyCoord(vlass_fields['RA'],vlass_fields['Dec'])

    coord = SkyCoord(12.767, -23.148, unit=u.deg)
    
    index = find_image(vlass_coords, coord)
    
    print(vlass_fields[index]['img_name'])
    
    

  #coord = SkyCoord(14.429, -27.013, unit=u.deg)
  
  #coord = SkyCoord("00h57m42.9s -27d00m46.5s")
  
  #coord = SkyCoord(14.504, -23.914, unit=u.deg)
  
  #coord = SkyCoord(13.948, -27.076, unit=u.deg)

  #search_fields(coord, vlass_fields)

  #print(coord)
  #print(coord.to_string('hmsdms',sep=':'))
