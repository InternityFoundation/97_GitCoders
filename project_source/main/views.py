from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from .models import *
#from .views import *
from .forms import *
from django.core.files import File
import copy
from keras.models import model_from_json
from keras import backend as K
import cv2
import numpy as np
import json
import base64 
from PIL import Image
import os
import argparse
#import numpy as np
#import cv2
from .utils import *
from .background_marker import *
#import cv2
from tqdm import tqdm
import itertools
# from django.shortcuts import render, redirect
from sklearn.externals import joblib
from sklearn.ensemble import GradientBoostingRegressor

#import numpy as np
#import matplotlib.pyplot as plt
#import json
#from keras.models import model_from_json

#project_path = 'D:/plant_disease_prediction/project source/'
project_path = '/home/rajat/workspace/code-n-counter/CropCare/project source/'
static_path = '/home/rajat/workspace/code-n-counter/CropCare/static_cdn/media_root/'


from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .market_price import find_nearest_city_market
import sys
from .darkflow.cli import cliHandler

class HomePageView( TemplateView):
    template_name = "index.html"
    
def predict_soil_health(N, P, K, C, pH, temp):
    x = [[N, P, K, C, pH, temp]]
    loaded_model = joblib.load(project_path+'main/soil_health_weights.pkl')  
    output = loaded_model.predict(x)[0]
    print(output)
    health = (output - 1000) / (2500 - 1000)
    #print(health*100)
    return health*100

def predict_livestock_health(surgery, age, respiratory_rate, rectal_temp, pulse, mucous_membrane):
    # 'No','adult', 28, 38.5, 66, 'pale_cyanotic'
    # 'young'
    if surgery == "Yes" :
        surgery = 1
    else:
        surgery = 0
   
    if age == "adult" :
        age = 1
    else:
        age = 2
       
    if mucous_membrane == 'bright_pink':
        mucous_membrane = 0
    elif mucous_membrane == 'bright_red':
        mucous_membrane = 1
    elif mucous_membrane == 'dark_cyanotic':
        mucous_membrane = 2
    elif mucous_membrane == 'normal_pink':
        mucous_membrane = 3
    elif mucous_membrane == 'pale_cyanotic':
        mucous_membrane = 4
    else: #pale_pink
        mucous_membrane = 5
   
   
    x = [[surgery, age, respiratory_rate, rectal_temp, pulse, mucous_membrane]]
    loaded_model = joblib.load(project_path+'main/cattle_health_weights.pkl')  
    output = loaded_model.predict(x)[0]
   
    if output==0:
        return "Chronic Disease"
    elif output==1:
        return "Acute Disease"
    else:
        return "Healthy"

@login_required(login_url='/')
def dashboard(request):
    
    city = request.GET.get('city', 'Ghaziabad')
    print('####',city)
    market_price = find_nearest_city_market(city)
    market1_city = list(market_price[0].keys())[0]
    market2_city = list(market_price[1].keys())[0]
    market3_city = list(market_price[2].keys())[0]
    market4_city = list(market_price[3].keys())[0]
    print(market4_city)
    market1 = market_price[0][list(market_price[0].keys())[0]]
    market2 = market_price[1][list(market_price[1].keys())[0]]
    market3 = market_price[2][list(market_price[2].keys())[0]]
    market4 = market_price[3][market4_city]
    print(market4)

    return render(request, 'dashboard/dashboard-home.html',{
        'market1_city': market1_city,
        'market2_city': market2_city,
        'market3_city': market3_city,
        'market4_city': market4_city,
        'market1': market1,
        'market2': market2,
        'market3': market3,
        'market4': market4,
        'market_price': market_price[0],'market_price_secondary': market_price[:1]})

class Dashboard(TemplateView):
    template_name = "dashboard/dashboard-home.html"
    
class DashboardUpload(TemplateView):
    template_name = "dashboard/upload-image.html"
    
def LivestockHealthcare(request):
    if request.method == 'POST':
        try:
            surgery = request.POST.get('surgery')
            age = request.POST.get('age')
            respiratory_rate = request.POST.get('respiratory_rate')
            rectal_temp = request.POST.get('rectal_temp')
            pulse = request.POST.get('pulse')
            mucous_membrane = request.POST.get('mucous_membrane')
            # print(nitrogen, phosphorous, potasium, calcium, ph, temp)
            x = predict_livestock_health(surgery, age, respiratory_rate, rectal_temp, pulse, mucous_membrane)
            # x = predict_soil_health(398,49,257, .6235 ,6.901,29)
        
            message = "Livestock status: "+ x
            return render(request, 'dashboard/livestock-healthcare-result.html',{'message': message})
        except:
            message = "Parameter not passed"
            return render(request, 'dashboard/livestock-healthcare-result.html',{'message': message})

    # print("#####", predict_soil_health('No','adult', 28, 38.5, 66, 'pale_cyanotic'))
    # 'No','adult', 28, 38.5, 66, 'pale_cyanotic'
    return render(request, 'dashboard/livestock-healthcare.html')

def SoilHealthcare(request):
    if request.method == 'POST':
        try:
            nitrogen = request.POST.get('nitrogen')
            phosphorous = request.POST.get('phosphorous')
            potasium = request.POST.get('potasium')
            calcium = request.POST.get('calcium')
            ph = request.POST.get('ph')
            temp = request.POST.get('temp')
            # print(nitrogen, phosphorous, potasium, calcium, ph, temp)
            x = predict_soil_health(nitrogen, phosphorous, potasium, calcium, ph, temp)
            # x = predict_soil_health(398,49,257, .6235 ,6.901,29)
            print(nitrogen, phosphorous, potasium, calcium, ph, temp, x)
            results = []
            if int(x) < 40:
                message = "Soil is in poor condition"
            if int(x) < 70:
                message = "Soil is in moderate condition"
            else:
                message = "Soil is in good condition"
            if float(ph) <5.5:
                results.append('It is too acidic for most of the agricultural crops so lime is needed.')
            elif float(ph) <8:
                results.append('This soil does not need any lime.')
            else:
                results.append("The very high PH indicates that this soil is calcareous. ")

            if float(potasium) < 260:
                results.append('Potasium is low')
            else:
                results.append('There is sufficient amount of Potasium')

            if float(phosphorous) < 45:
                results.append('Phosphorous is low')
            else:
                results.append('There is sufficient amount of Phosphorous')

            if float(calcium) < .5:
                results.append('Calcium is low')
            else:
                results.append('There is sufficient amount of Calcium')

            if float(nitrogen) < 350:
                results.append('Nitrogen is low')
            else:
                results.append('There is sufficient amount of Nitrogen')

            return render(request, 'dashboard/soil-healthcare-result.html',{'message': message,  'results': results})
        except:
            message = "Parameter not passed"
            return render(request, 'dashboard/soil-healthcare-result.html',{'message': message})

    return render(request, 'dashboard/soil-healthcare.html')
    # template_name = "dashboard/soil-healthcare.html"
    


def generate_background_marker(file):
    """
    Generate background marker for an image

    Args:
        file (string): full path of an image file

    Returns:
        tuple[0] (ndarray of an image): original image
        tuple[1] (ndarray size of an image): background marker
    """

    # check file name validity
    if not os.path.isfile(file):
        raise ValueError('{}: is not a file'.format(file))

    original_image = read_image(file)

    marker = np.full((original_image.shape[0], original_image.shape[1]), True)

    # update marker based on vegetation color index technique
    color_index_marker(index_diff(original_image), marker)

    # update marker to remove blues
    # remove_blues(original_image, marker)

    return original_image, marker


def segment_leaf(image_file, filling_mode, smooth_boundary, marker_intensity):
    """
    Segments leaf from an image file

    Args:
        image_file (string): full path of an image file
        filling_mode (string {no, flood, threshold, morph}):
            how holes should be filled in segmented leaf
        smooth_boundary (boolean): should leaf boundary smoothed or not
        marker_intensity (int in rgb_range): should output background marker based
                                             on this intensity value as foreground value

    Returns:
        tuple[0] (ndarray): original image to be segmented
        tuple[1] (ndarray): A mask to indicate where leaf is in the image
                            or the segmented image based on marker_intensity value
    """
    # get background marker and original image
    original, marker = generate_background_marker(image_file)

    # set up binary image for futher processing
    bin_image = np.zeros((original.shape[0], original.shape[1]))
    bin_image[marker] = 255
    bin_image = bin_image.astype(np.uint8)

    # further processing of image, filling holes, smoothing edges
    largest_mask = select_largest_obj(bin_image, fill_mode=filling_mode,
                           smooth_boundary=smooth_boundary)

    if marker_intensity > 0:
        largest_mask[largest_mask != 0] = marker_intensity
        image = largest_mask
    else:
        # apply marker to original image
        image = original.copy()
        image[largest_mask == 0] = np.array([0, 0, 0])

    return original, image


def rgb_range(arg):
    """
    Check if arg is in range for rgb value(between 0 and 255)

    Args:
        arg (int convertible): value to be checked for validity of range

    Returns:
        arg in int form if valid

    Raises:
        argparse.ArgumentTypeError: if value can not be integer or not in valid range
    """

    try:
        value = int(arg)
    except ValueError as err:
        raise argparse.ArgumentTypeError(str(err))

    if value < 0 or value > 255:
        message = "Expected 0 <= value <= 255, got value = {}".format(value)
        raise argparse.ArgumentTypeError(message)

    return value


def segment(image_source):
    marker_intensity=0
    fill='flood'
    smooth=True
    destination="test images/"

    # set up command line arguments conveniently
    filling_mode = FILL[fill.upper()]

#    folder, file = os.path.split(image_source)
#    files = [file]
#    base_folder = folder
#    if destination:
#        destination = destination
#    else:
#        destination = folder
    #print(files)

#    for file in files:
    # read image and segment leaf
    #print(os.path.join(base_folder, file))
    original, output_image = segment_leaf(image_source, filling_mode, smooth, marker_intensity)

    # handle destination folder and fileaname
#    filename, ext = os.path.splitext(file)

#    new_filename = filename + '_marked' + ext
#    new_filename = os.path.join(destination, new_filename)

    # change grayscale image to color image format i.e need 3 channels
#    if marker_intensity > 0:
#        output_image = cv2.cvtColor(output_image, cv2.COLOR_GRAY2RGB)

    # write the output
    #cv2.imwrite(new_filename, output_image)
    return output_image


def predict_disease(filename ,filemarked, pk):
    
    img = cv2.imread(static_path+filemarked)
    
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    stencil = np.zeros(img.shape).astype(img.dtype)

    c=[255,0,0]
    indices = np.where(np.all(img == c, axis=-1))
    a=indices[1]
    b=indices[0]
    
    without_mark=False

    if len(a)!=0 and len(b)==0 and len(c)==0 and len(d)==0:
        x_mn=min(a)
        x_mx=max(a)
        y_mn=min(b)
        y_mx=max(b)
        #print(x_mn,x_mx)
        #print(y_mn,y_mx)

        img_org = cv2.imread(static_path+filename)
        img_org=cv2.cvtColor(img_org,cv2.COLOR_BGR2RGB)
        img_org = cv2.resize(img_org, (256, 256))
        cv2.imwrite("res1.png", img_org)
        indices=np.concatenate((np.expand_dims(a,1),np.expand_dims(b,1)),axis=1)
        contours=[indices]
        stencil = np.zeros(img.shape).astype(img.dtype)
        img2=cv2.drawContours(stencil,contours,-1,(255,255,255),thickness=cv2.FILLED)
        result = cv2.bitwise_and(img_org,img2)
        result=result[y_mn:y_mx,x_mn:x_mx]
        #plt.imshow(result)
        cv2.imwrite("res.png", result)

        upload_obj = UploadFile.objects.filter(id = pk)
        if upload_obj.exists():
            upload_obj = upload_obj.first()
            upload_obj.segmented.save("res.png", File(open("res.png", "rb")))
            upload_obj.save()
    else:
        without_mark=True

    ######################
    json_file = open(project_path+'main/weights/VGG16_onlycropdetect/VGG16_onlycropdetect_model.json', 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    # load weights into new model

    model.load_weights(project_path+"main/weights/VGG16_onlycropdetect/vgg16_onlycropdetect__best.hdf5")

    with open(project_path+'main/labels/crop_labels.json', 'r') as fp:
        dic = json.load(fp)

    if without_mark:
        im = segment(project_path+'res1.png')
    else:
        im = segment(project_path+'res.png')

    im = cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), (256, 256))
    #plt.imshow(im)
    im = np.expand_dims(im, axis =0)
    im=cv2.normalize(im.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)


    outcome=model.predict(im)
    K.clear_session()
    pred=np.argmax(outcome)
    crop_label_predicted=dic[str(pred)]


    json_model_path=project_path+'main/weights/VGG16_'+crop_label_predicted+'_model.json'
    saved_weight_path=project_path+'main/weights/vgg16_best_'+crop_label_predicted+'.hdf5'
    label_path=project_path+'main/labels/'+crop_label_predicted+'_label.json'

    json_file = open(json_model_path, 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    # load weights into new model
    model.load_weights(saved_weight_path)
    #print("Loaded model from disk")


    with open(label_path, 'r') as fp:
        dic = json.load(fp)

    outcome=model.predict(im)
    K.clear_session()
    pred=sorted(((e,i) for i,e in enumerate(outcome[0])),reverse=True)

    out=[]
    for x in pred:
        #print("predited class:",dic[str(x[1])],"  with confidence: ",x[0]*100,"%")
        out.append((dic[str(x[1])],x[0]*100))

    return out


#
#def predict_disease(filename):
#
#    json_file = open(project_path+'main/weights/VGG16_onlycropdetect/VGG16_onlycropdetect_model.json', 'r')
#    model_json = json_file.read()
#    json_file.close()
#    model = model_from_json(model_json)
#
#    model.load_weights(project_path+"main/weights/VGG16_onlycropdetect/vgg16_onlycropdetect__best.hdf5")
#
#    with open(project_path+'main/labels/crop_labels.json', 'r') as fp:
#        dic = json.load(fp)
#
#    im = segment(static_path+filename)
#
#    im = cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), (256, 256))
#    im = np.expand_dims(im, axis =0)
#    im=cv2.normalize(im.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
#
#
#    outcome=model.predict(im)
#    K.clear_session()
#    pred=np.argmax(outcome)
#    crop_label_predicted=dic[str(pred)]
#
#
#    json_model_path=project_path+'main/weights/VGG16_'+crop_label_predicted+'_model.json'
#    saved_weight_path=project_path+'main/weights/vgg16_best_'+crop_label_predicted+'.hdf5'
#    label_path=project_path+'main/labels/'+crop_label_predicted+'_label.json'
#
#    json_file = open(json_model_path, 'r')
#    model_json = json_file.read()
#    json_file.close()
#    model = model_from_json(model_json)
#    model.load_weights(saved_weight_path)
#
#
#    with open(label_path, 'r') as fp:
#        dic = json.load(fp)
#
#    outcome=model.predict(im)
#    K.clear_session()
#    pred=sorted(((e,i) for i,e in enumerate(outcome[0])),reverse=True)
#
#    out=[]
#    for x in pred:
#        out.append((dic[str(x[1])],x[0]*100))
#
#    return out

# for uploading to yolo model
def upload_cassava_leaf(request):
    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.name = f.image
            f.save()
#            print("Path is",f.image)
            # im = Image.open(static_path+str(f.image))
            im = cv2.imread(static_path+str(f.image))
            im = cv2.resize(im, (608,608))
            cv2.imwrite("test/images/convert.jpg", im)
            # im.save('test/images/convert.jpg')
        try:
            cliHandler(['flow', '--model', 'cfg/yolo-new.cfg', '--imgdir', 'test/images', '--load', '-1', '--labels', 'labels.txt'])
            f.edited.save("abc.png", File(open("test/images/out/convert.jpg", "rb")))
            result_obj = UploadFile.objects.get(id = f.id)
            print('####', result_obj)
            return render(request, 'dashboard/cassava_leaf_result.html', {'image': result_obj})

        except:
            print("Error in the show")
            return render(request, 'dashboard/cassava_leaf_result.html', {'message': 'System Mistake! Please click again!'})
    
        return HttpResponse("Image Not Received")
    else:
        form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request,'upload-leaf.html',context)


def upload_leaf(request):
    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.name = f.image
            f.save()
#            print("Path is",f.image)
            im = Image.open(static_path+str(f.image))
            im.save('convert.png')
            f.image.save("convert.png", File(open("convert.png", "rb")))
            f.edited = f.image
            f.save()
    
            return redirect('/edit/'+str(f.id))
        return HttpResponse("Image Not Received")
#            return render(request,'edit.html',context)
    else:
        form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request,'upload-leaf.html',context)

class plant_result():
    def __init__(self,plant, disease,accuracy):
        self.plant = plant
        self.disease = disease
        self.accuracy = accuracy


from googletrans import Translator


def result(request,pk,lang='eng'):
    translator = Translator()
    
#    translator = Translator()
    lang_flag = True
    if lang == 'hindi':
        target_lang = 'hi'
    elif lang == 'tamil':
        target_lang = 'ta'
    elif lang == 'punjabi':
        target_lang = 'pa'
    else:
        target_lang = 'en'
        lang_flag = False
    
    upload_obj = UploadFile.objects.filter(id = pk)
    if upload_obj.exists():
        upload_obj = upload_obj.first()
        if upload_obj.edited:
            result = predict_disease(str(upload_obj.image),str(upload_obj.edited),pk)
        else:
            result = predict_disease(str(upload_obj.image),str(upload_obj.image),pk)

        print(result)
        more_result = result[1:]
#        result=[0]
        
        result_count = len(result)-1
        if (result_count > 2):
            result_count = 2

        other_predicted_results=[]
        for i in range(1,result_count+1):
            x,y = result[i][0].split('___')
            y = ' '.join(y.split('_'))
            acc = round(result[i][1],2)
            other_predicted_results.append(plant_result(x,y,acc))

        main_result_name = result[0][0]
        main_result_accuracy = round(result[0][1],2)
        plant, disease = main_result_name.split('___')
        plant = ' '.join(plant.split('_'))
        disease = ' '.join(disease.split('_'))
        print("Plant:",plant)
        print("Disease:",disease)
        plant_obj = Plant.objects.filter( Q(name__icontains=plant)).first()
        disease_obj = Disease.objects.filter(Q(name__icontains=disease)).filter(plant = plant_obj).first()
        
#        disease_obj_lang = copy.deepcopy(disease_obj)
        if lang_flag:
            disease_obj.name = disease_obj.name + '('+ translator.translate(disease_obj.name, dest=target_lang).text +')'
        disease_obj.symptoms = translator.translate(disease_obj.symptoms, dest=target_lang).text
        disease_obj.cause = translator.translate(disease_obj.cause, dest=target_lang).text
        disease_obj.comments = translator.translate(disease_obj.comments, dest=target_lang).text
        disease_obj.management = translator.translate(disease_obj.management, dest=target_lang).text
        prediction_result_text = translator.translate('Prediction Results', dest=target_lang).text
        might_also_be_text = translator.translate('Might Also Be', dest=target_lang).text
        plant = translator.translate(plant, dest=target_lang).text
        context ={
            "disease": disease_obj,
            "prediction_result_text": prediction_result_text,
            "might_also_be_text": might_also_be_text,
            "plant": plant,
            "main_accuracy": main_result_accuracy,
            "upload": upload_obj,
            "other_results": other_predicted_results,
            "pk": pk,
        }
        return render(request,'result.html',context)
    else:
        return HttpResponse("Error in result")

def edit(request,pk):
    if request.method == "POST":
                
        json_data = json.loads(request.body) 
#        print("data: ",json_data)
        try:
#            obj_id = json_data['id']
            image_string = json_data['image']
            file_format = image_string.split(';')[0].split('/')[1]
            image_data = image_string.split('base64,')[1]
            with open("image" + "." + file_format, "wb") as fh:
                fh.write(base64.decodebytes(bytes(image_data, "utf-8")))
                django_file = fh
                upload_obj = UploadFile.objects.filter(id = pk)
                if upload_obj.exists():
                    upload_obj = upload_obj.first()
                    upload_obj.edited.save("image" + "." + file_format, File(open("image" + "." + file_format, "rb")))
                    upload_obj.save()
                    print("done")
#                    return redirect('/result/'+str(pk))
                else:
                    print("object error")
            
        except KeyError:
            print("error")

    file_obj = UploadFile.objects.filter(id = pk)
    if file_obj.exists():
        file_obj = file_obj.first()
        context ={
            "file": file_obj,
            "pk": pk
        }
        return render(request,'edit.html',context)
    else:
        return HttpResponse("UploadFile object not found")

