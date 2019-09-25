import astropy.units as u
from astropy.io import fits
from astropy.table import Table
from os.path import join
import os
import numpy as np

base_folder = '/import/ada2/vlass/'

filename = '/import/ada2/ddob1600/vlass_images/VLASS1.1/T01t02/VLASS1.1.ql.T01t02.J003230-373000.10.2048.v1/VLASS1.1.ql.T01t02.J003230-373000.10.2048.v1.I.iter1.image.pbcor.tt0.subim.fits'



img_info = []

def get_img_info(img_name):
  hdulist = fits.open(img_name)
  header = hdulist[0].header
  ra = header['CRVAL1']
  dec = header['CRVAL2']
  obs_date = header['DATE-OBS']
  
  return [ra,dec,obs_date,img_name]
  

for epoch_folder in os.listdir(base_folder):
  for tile_folder in os.listdir(join(base_folder,epoch_folder)):
    for img_folder in os.listdir(join(base_folder,epoch_folder,tile_folder)):
      filenames = os.listdir(join(base_folder,epoch_folder,tile_folder,img_folder))
      
      img_file_name = img_folder+'.I.iter1.image.pbcor.tt0.subim.fits'
      img_file = join(base_folder,epoch_folder,tile_folder,img_folder,img_file_name)
      
      img_info.append(get_img_info(img_file))

#print(img_info.shape)
image_table = Table(rows=np.asarray(img_info), names=('RA','Dec','obs_date','img_name'))

image_table.write('vlass_imagelist.csv', overwrite=True)





