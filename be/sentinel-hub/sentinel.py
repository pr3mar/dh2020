from sentinelhub import SHConfig
from datetime import datetime,timedelta
import numpy as np
from math import cos,radians
import sys,csv
import matplotlib.pyplot as plt
from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox, DataCollection,WebFeatureService,SentinelHubRequest
from sentinelhub.geo_utils import bbox_to_dimensions

from oauthlib.oauth2 import BackendApplicationClient
import imageio


INSTANCE_ID = ''  # In case you put instance ID into configuration file you can leave this unchanged

if INSTANCE_ID:
    config = SHConfig()
    config.instance_id = INSTANCE_ID
else:
    config = None


def plot_image(image, factor=1):
    """
    Utility function for plotting RGB images.
    """
    fig = plt.subplots(nrows=1, ncols=1, figsize=(15, 7))

    if np.issubdtype(image.dtype, np.floating):
        plt.imshow(np.minimum(image * factor, 1))
        plt.show()
    else:
        plt.imshow(image)
        plt.show()

def get_bounding_box(latitude,longtitude,radius=1):
    dLat = radius / 111.1
    dLon = dLat / cos(radians(latitude))
    bounding_box_coord = [longtitude-dLon,latitude - dLat,longtitude+dLon,latitude+dLat]
    # print(bounding_box_coord)
    return BBox(bbox=bounding_box_coord, crs=CRS.WGS84) 

def get_available_dates(bounding_box,time_interval):
    wfs = WebFeatureService(bbox=bounding_box, time_interval=time_interval,
                        config=config)
                        
    return [date_time.strftime('%Y-%m-%d') for date_time in wfs.get_dates()]

def get_image_data(datum,bounding_box,config):
    evalscript_true_color = """
    //VERSION=3

    function setup() {
        return {
            input: [{
                bands: ["B02", "B03", "B04"]
            }],
            output: {
                bands: 3
            }
        };
    }

    function evaluatePixel(sample) {
        return [3.5*sample.B04, 3.5*sample.B03, 3.5*sample.B02];
    }
    """

    request = SentinelHubRequest(
        evalscript=evalscript_true_color,
        input_data=[
            SentinelHubRequest.input_data(
                data_collection=DataCollection.SENTINEL2_L1C,
                time_interval=datum)
        ],
        responses=[
            SentinelHubRequest.output_response(
                'default', MimeType.PNG)],
        bbox=bounding_box,
        size=(1000,1000),
        config=config)

    return request.get_data()[0]

def parse_date(date):
    out_date = datetime.strptime(date, '%d %B %Y')
    return datetime.strftime(out_date,'%Y-%m-%d')

def parse_input_data():
    output_data = []
    with open(sys.argv[1],newline='') as in_file:
        data = csv.reader(in_file,delimiter=',')
        next(data)
        for row in data:
            print(row)
            spill,location,date,min_tones,max_tonnes,owner,lat,lon = row
            output_data.append([spill,location,parse_date(date),float(lat),float(lon)])
    return output_data






for site in parse_input_data()[1:]:
    spill,location,dat,lat,lon = site
    bb =get_bounding_box(lat,lon,1)
    interval_from = datetime.strptime(dat,'%Y-%m-%d') - timedelta(days=30)
    interval_to = datetime.strptime(dat,'%Y-%m-%d') + timedelta(days=30)
    available_dates = get_available_dates(bb,(interval_from,interval_to))
    for dat in available_dates:
        image = get_image_data(dat,bb,config)
        imageio.imwrite("_".join(['imgs_/image',spill,dat])+'.jpg',image)


# from pyproj import Geod

# Geod()

