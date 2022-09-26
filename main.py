from osgeo import gdal
from osgeo import ogr
from osgeo import gdalconst as GConst

import sys

import shutil

def readWriteGDAL ():
    """ read and write GDAL functionality """

    ds = gdal.Open ("data/carroll_nccpi.tif", GConst.GA_ReadOnly)
    band = ds.GetRasterBand (1)
    data = band.ReadAsArray ()
    x = band.XSize
    y = band.YSize
    sys.stdout.write (f"Read {x} * {y} data array\n")

    ds = None # noqa

    shutil.copy ("data/carroll_nccpi.tif", "data/out.tif")
    ods = gdal.Open ("data/out.tif", GConst.GA_Update)
    oband = ods.GetRasterBand (1)
    oband.WriteArray (data)
    sys.stdout.write (f"Wrote {x} * {y} data array\n\n")

    ods = None # noqa

def readTestOGR ():
    """ read/write vectort graphics """
    ds = ogr.Open ("data/us_states.json", GConst.GF_Read)
    layer = ds.GetLayer ()

    features = []
    for f in layer:
        features.append (f)

    ds = None # noqa

    sys.stdout.write (f"Read {len (features)} features.\n")


if __name__ == "__main__":
    """ entry point """

    readWriteGDAL ()
    readTestOGR ()



