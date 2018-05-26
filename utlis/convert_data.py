import scipy.io as io
import os
import json
from pprint import pprint
def load_data(fname):
  '''
  anno file format:
      train_anno =['__header__':heading, '__version__':version, '__globals__':global, 'annotations':annotation]
  annotation's format:
      shape : [1,m]
      inside each example:
          bbox_x1: Min x-value of the bounding box, in pixels
          bbox_y1: Max x-value of the bounding box, in pixels
          bbox_x2: Min y-value of the bounding box, in pixels
          bbox_y2: Max y-value of the bounding box, in pixels
          class: Integral id of the class the image belongs to.
          fname: Filename of the image within the folder of images.
  test_anno is the same but don't have class
  return: annotations data only
  '''
  data_path = '../data/annotations/'
  anno_path = os.path.join(data_path,fname)
  data  = io.loadmat(anno_path)
  return data['annotations'][0]

def convert_to_json(annof):
  trunk = [[] for _ in range(49)]
  '''
  output format:
  { 'filename': '28503151_5b5b7ec140_b.jpg',
    'regions': {
        '0': {
            'region_attributes': {},
            'shape_attributes': {
                'all_points_x': [...],
                'all_points_y': [...],
                'name': 'polygon'}},
        ... more regions ...
    },
    'size': 100202
  }
  '''
  trunk = {
      'AM' : [],
      'Acura' : [],
      'Aston' : [],
      'Audi' : [],
      'BMW' : [],
      'Bentley' : [],
      'Bugatti' : [],
      'Buick' : [],
      'Cadillac' : [],
      'Chevrolet' : [],
      'Chrysler' : [],
      'Daewoo' : [],
      'Dodge' : [],
      'Eagle' : [],
      'FIAT' : [],
      'Ferrari' : [],
      'Fisker' : [],
      'Ford' : [],
      'GMC' : [],
      'Geo' : [],
      'HUMMER' : [],
      'Honda' : [],
      'Hyundai' : [],
      'Infiniti' : [],
      'Isuzu' : [],
      'Jaguar' : [],
      'Jeep' : [],
      'Lamborghini' : [],
      'Land' : [],
      'Lincoln' : [],
      'MINI' : [],
      'Maybach' : [],
      'Mazda' : [],
      'McLaren' : [],
      'Mercedes-Benz': [],
      'Mitsubishi' : [],
      'Nissan' : [],
      'Plymouth' : [],
      'Porsche' : [],
      'Ram' : [],
      'Rolls-Royce': [],
      'Scion' : [],
      'Spyker' : [],
      'Suzuki' : [],
      'Tesla' : [],
      'Toyota' : [],
      'Volkswagen' : [],
      'Volvo' : [],
      'smart' : [],
  }

  id={
      0:'AM',
      1:'Acura',
      2:'Acura',
      3:'Acura',
      4:'Acura',
      5:'Acura',
      6:'Acura',
      7:'Aston',
      8:'Aston',
      9:'Aston',
      10:'Aston',
      11:'Audi',
      12:'Audi',
      13:'Audi',
      14:'Audi',
      15:'Audi',
      16:'Audi',
      17:'Audi',
      18:'Audi',
      19:'Audi',
      20:'Audi',
      21:'Audi',
      22:'Audi',
      23:'Audi',
      24:'Audi',
      25:'BMW',
      26:'BMW',
      27:'BMW',
      28:'BMW',
      29:'BMW',
      30:'BMW',
      31:'BMW',
      32:'BMW',
      33:'BMW',
      34:'BMW',
      35:'BMW',
      36:'BMW',
      37:'BMW',
      38:'Bentley',
      39:'Bentley',
      40:'Bentley',
      41:'Bentley',
      42:'Bentley',
      43:'Bentley',
      44:'Bugatti',
      45:'Bugatti',
      46:'Buick',
      47:'Buick',
      48:'Buick',
      49:'Buick',
      50:'Cadillac',
      51:'Cadillac',
      52:'Cadillac',
      53:'Chevrolet',
      54:'Chevrolet',
      55:'Chevrolet',
      56:'Chevrolet',
      57:'Chevrolet',
      58:'Chevrolet',
      59:'Chevrolet',
      60:'Chevrolet',
      61:'Chevrolet',
      62:'Chevrolet',
      63:'Chevrolet',
      64:'Chevrolet',
      65:'Chevrolet',
      66:'Chevrolet',
      67:'Chevrolet',
      68:'Chevrolet',
      69:'Chevrolet',
      70:'Chevrolet',
      71:'Chevrolet',
      72:'Chevrolet',
      73:'Chevrolet',
      74:'Chevrolet',
      75:'Chrysler',
      76:'Chrysler',
      77:'Chrysler',
      78:'Chrysler',
      79:'Chrysler',
      80:'Chrysler',
      81:'Daewoo',
      82:'Dodge',
      83:'Dodge',
      84:'Dodge',
      85:'Dodge',
      86:'Dodge',
      87:'Dodge',
      88:'Dodge',
      89:'Dodge',
      90:'Dodge',
      91:'Dodge',
      92:'Dodge',
      93:'Dodge',
      94:'Dodge',
      95:'Dodge',
      96:'Dodge',
      97:'Eagle',
      98:'FIAT',
      99:'FIAT',
      100:'Ferrari',
      101:'Ferrari',
      102:'Ferrari',
      103:'Ferrari',
      104:'Fisker',
      105:'Ford',
      106:'Ford',
      107:'Ford',
      108:'Ford',
      109:'Ford',
      110:'Ford',
      111:'Ford',
      112:'Ford',
      113:'Ford',
      114:'Ford',
      115:'Ford',
      116:'Ford',
      117:'GMC',
      118:'GMC',
      119:'GMC',
      120:'GMC',
      121:'GMC',
      122:'Geo',
      123:'HUMMER',
      124:'HUMMER',
      125:'Honda',
      126:'Honda',
      127:'Honda',
      128:'Honda',
      129:'Hyundai',
      130:'Hyundai',
      131:'Hyundai',
      132:'Hyundai',
      133:'Hyundai',
      134:'Hyundai',
      135:'Hyundai',
      136:'Hyundai',
      137:'Hyundai',
      138:'Hyundai',
      139:'Hyundai',
      140:'Infiniti',
      141:'Infiniti',
      142:'Isuzu',
      143:'Jaguar',
      144:'Jeep',
      145:'Jeep',
      146:'Jeep',
      147:'Jeep',
      148:'Jeep',
      149:'Lamborghini',
      150:'Lamborghini',
      151:'Lamborghini',
      152:'Lamborghini',
      153:'Land',
      154:'Land',
      155:'Lincoln',
      156:'MINI',
      157:'Maybach',
      158:'Mazda',
      159:'McLaren',
      160:'Mercedes-Benz',
      161:'Mercedes-Benz',
      162:'Mercedes-Benz',
      163:'Mercedes-Benz',
      164:'Mercedes-Benz',
      165:'Mercedes-Benz',
      166:'Mitsubishi',
      167:'Nissan',
      168:'Nissan',
      169:'Nissan',
      170:'Nissan',
      171:'Plymouth',
      172:'Porsche',
      173:'Ram',
      174:'Rolls-Royce',
      175:'Rolls-Royce',
      176:'Rolls-Royce',
      177:'Scion',
      178:'Spyker',
      179:'Spyker',
      180:'Suzuki',
      181:'Suzuki',
      182:'Suzuki',
      183:'Suzuki',
      184:'Tesla',
      185:'Toyota',
      186:'Toyota',
      187:'Toyota',
      188:'Toyota',
      189:'Volkswagen',
      190:'Volkswagen',
      191:'Volkswagen',
      192:'Volvo',
      193:'Volvo',
      194:'Volvo',
      195:'smart',
  }

  data = load_data(annof)
  json_anno =[]

  for anno in data:
    x1 = anno[0][0][0]
    y1 = anno[1][0][0]
    x2 = anno[2][0][0]
    y2 = anno[3][0][0]
    class_id = anno[4][0][0]
    fname = anno[5][0]
    all_points_x=[str(x1),str(x2),str(x2),str(x1)]
    all_points_y=[str(y1),str(y1),str(y2),str(y2)]
    data = {}
    size = os.path.getsize('../data/cars_train/'+fname)
    data= { 'filename': fname,
           'size': size,
           'regions': {
            '0': {
                'region_attributes': {},
                'shape_attributes': {
                    'all_points_x': all_points_x,
                    'all_points_y': all_points_y
                }
              },
            }
    }

    trunk[id[class_id-1]].append(data)
  for idx,key in enumerate(trunk.keys()):
    data_out = trunk[key]
    name = '../data/annotations/json/'+key.lower() + '.json'
    with open(name,'w') as f:
      json.dump(data_out,f,indent=2)


def main():
  '''
  {'AM': [0],
   'Acura': [1, 2, 3, 4, 5, 6],
   'Aston': [7, 8, 9, 10],
   'Audi': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
   'BMW': [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37],
   'Bentley': [38, 39, 40, 41, 42, 43],
   'Bugatti': [44, 45],
   'Buick': [46, 47, 48, 49],
   'Cadillac': [50, 51, 52],
   'Chevrolet': [53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74],
   'Chrysler': [75, 76, 77, 78, 79, 80],
   'Daewoo': [81],
   'Dodge': [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96],
   'Eagle': [97],
   'FIAT': [98, 99],
   'Ferrari': [100, 101, 102, 103],
   'Fisker': [104],
   'Ford': [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116],
   'GMC': [117, 118, 119, 120, 121],
   'Geo': [122],
   'HUMMER': [123, 124],
   'Honda': [125, 126, 127, 128],
   'Hyundai': [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139],
   'Infiniti': [140, 141],
   'Isuzu': [142],
   'Jaguar': [143],
   'Jeep': [144, 145, 146, 147, 148],
   'Lamborghini': [149, 150, 151, 152],
   'Land': [153, 154],
   'Lincoln': [155],
   'MINI': [156],
   'Maybach': [157],
   'Mazda': [158],
   'McLaren': [159],
   'Mercedes-Benz': [160, 161, 162, 163, 164, 165],
   'Mitsubishi': [166],
   'Nissan': [167, 168, 169, 170],
   'Plymouth': [171],
   'Porsche': [172],
   'Ram': [173],
   'Rolls-Royce': [174, 175, 176],
   'Scion': [177],
   'Spyker': [178, 179],
   'Suzuki': [180, 181, 182, 183],
   'Tesla': [184],
   'Toyota': [185, 186, 187, 188],
   'Volkswagen': [189, 190, 191],
   'Volvo': [192, 193, 194],
   'smart': [195]}
  '''
  convert_to_json('cars_train_annos')



if __name__ == '__main__':
  main()
