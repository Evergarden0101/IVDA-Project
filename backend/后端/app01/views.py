import json
import pycountry as pc
from django.shortcuts import render,HttpResponse
import pandas as pd
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# tem = pd.read_csv('./daily_temperature_1000_cities_1980_2020.csv',  skiprows=12)
tem = pd.read_csv('./daily_temperature_1000_cities_1980_2020.csv')
inf = pd.read_csv('./daily_temperature_1000_cities_1980_2020.csv', nrows=12).T
co2 = pd.read_csv('./fossil-fuel-co2-emissions-by-nation_csv.csv')


def index(request):
    return HttpResponse('hallo')


# data: {time: [1980,2020] //初始默认40年}
@csrf_exempt
def tempGeoJson(request):
    try:
        a = eval(request.GET['data'])
    except:
        a =None
    if a==None:
        first = 1980
        second = 2020
    else:

        if a.get('time') == '[1980,2020]':
            first =1980
            second = 2020
        else:
            first = int(a.get('time')[0])
            second = int(a.get('time')[1])

    firsttime = first
    secondtime = second
    info =inf.copy()
    info.columns = info.iloc[0]
    info = info.iloc[1:, :]

    a = info.groupby(by=['country'])
    csvlist = []

    for i in a['country'].sum().index:
        b = a.get_group(i)
        b.reset_index(inplace=True)
        diyi = i  # Australia
        dier = b['iso3'][0]  # AUS
        zzl_list = []
        for y in b['index']:
            newda = tem.iloc[:, [0, int(y) + 1]]
            newda = newda.loc[12:, ]
            newda['Unnamed: 0'] = pd.to_datetime(newda['Unnamed: 0'])
            # pdates = pd.date_range(start=firsttime, end=secondtime,closed='left')
            # newda_new = newda.reindex(pdates, fill_value=0)
            newda_new1 = newda.groupby(by=newda.iloc[:, 0].apply(lambda x: x.year))
            #         firsttime = firsttime
            daiqiu = newda_new1.get_group(int(firsttime))
            daiqiu.reset_index(inplace=True)
            # print(daiqiu.loc[:,y])
            daiqiu.loc[:,y] = pd.to_numeric(daiqiu.loc[:,y])
            # daiqiu[y] = pd.to_numeric(daiqiu.loc[:,y])
            first_tem = daiqiu[y].mean()
            daiqiu2 = newda_new1.get_group(int(secondtime))
            daiqiu2.reset_index(inplace=True)
            daiqiu2.loc[:, y] = pd.to_numeric(daiqiu2.loc[:, y])
            # daiqiu2[y] = pd.to_numeric(daiqiu2[y])
            second_tem = daiqiu2[y].mean()
            zzlv = (first_tem - second_tem) / second_tem
            zzl_list.append(zzlv)
        zuihou = format(np.mean(zzl_list), '.1%')
        csvlist.append([diyi, dier, zuihou])
    df = pd.DataFrame(csvlist,
                      columns=['name', 'code', 'tempRate']).to_json(orient='records')
    return JsonResponse(json.loads(df), safe=False)

@csrf_exempt
def co2GeoJson(request):
    global shuzhi
    try:
        a = eval(request.GET['data'])
    except:
        a = None
    if a == None:
        first = 1751
        second = 2014
    else:

        if a.get('time') == '[1751,2014]':
            first = 1751
            second = 2014
        else:
            first = int(a.get('time')[0])
            second = int(a.get('time')[1])

    firsttime = first
    secondtime = second
    co2a = co2.groupby(by=['Country'])
    co2_list = []
    for coun in co2a['Country'].sum().index:
        try:
            country = pc.countries.get(name=coun).alpha_3
            countryda = pc.countries.get(name=coun).name


            co2b = co2a.get_group(coun)
            co2b.reset_index(inplace=True)
            if co2b['Year'][0] <= firsttime and co2b['Year'][len(co2b['Year']) - 1] >= secondtime:
                shuzhi = (int(co2b.loc[co2b['Year'] == firsttime]['Total']) - int(
                    co2b.loc[co2b['Year'] == secondtime]['Total'])) / int(co2b.loc[co2b['Year'] == secondtime]['Total'])
            elif co2b['Year'][0] > firsttime and co2b['Year'][len(co2b['Year']) - 1] >= secondtime:
                shuzhi = (int(co2b['Total'][0]) - int(co2b.loc[co2b['Year'] == secondtime]['Total'])) / int(
                    co2b.loc[co2b['Year'] == secondtime]['Total'])
            elif co2b['Year'][0] > firsttime and co2b['Year'][len(co2b['Year']) - 1] < secondtime:
                shuzhi = (int(co2b['Total'][0]) - int(co2b['Total'][len(co2b['Year']) - 1])) / int(
                    co2b['Total'][len(co2b['Year']) - 1])
            elif co2b['Year'][0] <= firsttime and co2b['Year'][len(co2b['Year']) - 1] < secondtime:
                shuzhi = (int(co2b.loc[co2b['Year'] == firsttime]['Total'] - int(co2b['Total'][len(co2b['Year']) - 1])) / int(co2b['Total'][len(co2b['Year']) - 1]))


            zuihou = format(shuzhi, '.1%')
            co2_list.append([countryda, country, zuihou])
        except:
            pass
    df1 = pd.DataFrame(co2_list,
                      columns=['name', 'code', 'CO2Rate']).to_json(orient='records')
    return JsonResponse(json.loads(df1), safe=False)
@csrf_exempt
def monthTemp(request):
    a = eval(request.GET['data'])
    pdzhi =a.get('place')[1]
    guo = a.get('place')[0]
    if pdzhi == 0:
        newda = tem.loc[12:, ]
        newda['Unnamed: 0'] = pd.to_datetime(newda['Unnamed: 0'])
        newda_new1 = newda.groupby(by=newda.iloc[:, 0].apply(lambda x: x.year))
        all_data = []
        for i in range(1980, 2021):
            daiqiu = newda_new1.get_group(int(i))
            #     daiqiu.reset_index(inplace=True)
            newda_new2 = daiqiu.groupby(by=daiqiu.iloc[:, 0].apply(lambda x: x.month))
            for mo in range(1,13):
                molist = []
                # print(newda_new2.sum())
                try:
                    mo_daiqiu = newda_new2.get_group(int(mo))
                    mo_daiqiu.reset_index(inplace=True)
                    shuz = mo_daiqiu.iloc[:, 2:]
                    for shuliang in range(1000):
                        shuz[str(shuliang)] = pd.to_numeric(shuz[str(shuliang)])

                        molist.append(shuz[str(shuliang)].mean())
                    all_data.append([mo, i, np.mean(molist)])
                except:
                    pass
        df = pd.DataFrame(all_data,
                          columns=['Mon', 'Year', 'Temp']).to_json(orient='records')
        return JsonResponse(json.loads(df), safe=False)
    elif pdzhi == 1:#国家
        info = inf.copy()
        info.columns = info.iloc[0]
        info = info.iloc[1:, :]
        # info
        a = info.groupby(by=['iso3'])

        b = a.get_group(guo)
        b.reset_index(inplace=True)

        newda = tem.loc[12:, ]
        newda['Unnamed: 0'] = pd.to_datetime(newda['Unnamed: 0'])

        newda_new1 = newda.groupby(by=newda.iloc[:, 0].apply(lambda x: x.year))
        all_data = []
        for i in range(1980, 2021):
            daiqiu = newda_new1.get_group(int(i))
            newda_new2 = daiqiu.groupby(by=daiqiu.iloc[:, 0].apply(lambda x: x.month))
            for mo in range(1, 13):
                molist = []
                try:
                    mo_daiqiu = newda_new2.get_group(int(mo))
                    mo_daiqiu.reset_index(inplace=True)
                    shuz = mo_daiqiu.iloc[:, 1:]

                    for shuliang in b['index']:
                        newda_index = shuz.iloc[:, [0, int(shuliang) + 1]]
                        newda_index[str(shuliang)] = pd.to_numeric(newda_index[str(shuliang)])

                        molist.append(newda_index[str(shuliang)].mean())
                    all_data.append([mo, i, np.mean(molist)])
                except:
                    pass
        df = pd.DataFrame(all_data,
                          columns=['Mon', 'Year', 'Temp']).to_json(orient='records')
        return JsonResponse(json.loads(df), safe=False)
        # pass
    elif pdzhi ==2:
        info = inf.copy()
        info.columns = info.iloc[0]
        info = info.iloc[1:, :]
        # info
        a = info.groupby(by=['id'])

        b = a.get_group(guo)
        b.reset_index(inplace=True)

        newda = tem.loc[12:, ]
        newda['Unnamed: 0'] = pd.to_datetime(newda['Unnamed: 0'])
        # print(newda)
        newda_new1 = newda.groupby(by=newda.iloc[:, 0].apply(lambda x: x.year))
        all_data = []
        for i in range(1980, 2021):
            daiqiu = newda_new1.get_group(int(i))
            newda_new2 = daiqiu.groupby(by=daiqiu.iloc[:, 0].apply(lambda x: x.month))
            for mo in range(1, 13):
                molist = []
                try:
                    mo_daiqiu = newda_new2.get_group(int(mo))
                    mo_daiqiu.reset_index(inplace=True)
                    shuz = mo_daiqiu.iloc[:, 1:]

                    for shuliang in b['index']:
                        newda_index = shuz.iloc[:, [0, int(shuliang) + 1]]
                        newda_index[str(shuliang)] = pd.to_numeric(newda_index[str(shuliang)])

                        molist.append(newda_index[str(shuliang)].mean())
                    all_data.append([mo, i, np.mean(molist)])
                except:
                    pass
        df = pd.DataFrame(all_data,
                          columns=['Mon', 'Year', 'Temp']).to_json(orient='records')
        return JsonResponse(json.loads(df), safe=False)

def selectcountry(request):
    a = eval(request.GET['data'])
    print(a)
    # pdzhi =a.get('place')[1]
    if str(a.get('time')) == '[1980,2020]':
        first =1980
        second = 2020
    else:
        first = int(a.get('time')[0])
        second = int(a.get('time')[1])
    country = str(a.get('country'))
    info = inf.copy()
    info.columns = info.iloc[0]
    info = info.iloc[1:, :]
    # info
    # country = 'CHN'
    a = info.groupby(by=['iso3'])

    b = a.get_group(country)
    b.reset_index(inplace=True)

    firsttime = first
    secondtime = second

    di_lst = []
    digui = 0
    for y in b['index']:
        newda = tem.iloc[:, [0, int(y) + 1]]
        newda = newda.loc[12:, ]

        newda['Unnamed: 0'] = pd.to_datetime(newda['Unnamed: 0'])
        # pdates = pd.date_range(start=firsttime, end=secondtime,closed='left')
        # newda_new = newda.reindex(pdates, fill_value=0)
        newda_new1 = newda.groupby(by=newda.iloc[:, 0].apply(lambda x: x.year))
        #         firsttime = firsttime
        daiqiu = newda_new1.get_group(int(firsttime))
        daiqiu.reset_index(inplace=True)
        # print(daiqiu.loc[:,y])
        daiqiu.loc[:, y] = pd.to_numeric(daiqiu.loc[:, y])
        # daiqiu[y] = pd.to_numeric(daiqiu.loc[:,y])
        first_tem = daiqiu[y].mean()
        daiqiu2 = newda_new1.get_group(int(secondtime))
        daiqiu2.reset_index(inplace=True)
        daiqiu2.loc[:, y] = pd.to_numeric(daiqiu2.loc[:, y])
        # daiqiu2[y] = pd.to_numeric(daiqiu2[y])
        second_tem = daiqiu2[y].mean()
        zzlv = (first_tem - second_tem) / second_tem

        zuihou = format(zzlv, '.1%')

        try:
            global shuzhi
            countryda = pc.countries.get(alpha_3=country).name
            co2a = co2.groupby(by=['Country'])

            co2b = co2a.get_group(countryda)
            co2b.reset_index(inplace=True)
            if co2b['Year'][0] <= firsttime and co2b['Year'][len(co2b['Year']) - 1] >= secondtime:
                shuzhi = (int(co2b.loc[co2b['Year'] == firsttime]['Total']) - int(
                    co2b.loc[co2b['Year'] == secondtime]['Total'])) / int(co2b.loc[co2b['Year'] == secondtime]['Total'])
            elif co2b['Year'][0] > firsttime and co2b['Year'][len(co2b['Year']) - 1] >= secondtime:
                shuzhi = (int(co2b['Total'][0]) - int(co2b.loc[co2b['Year'] == secondtime]['Total'])) / int(
                    co2b.loc[co2b['Year'] == secondtime]['Total'])
            elif co2b['Year'][0] > firsttime and co2b['Year'][len(co2b['Year']) - 1] < secondtime:
                shuzhi = (int(co2b['Total'][0]) - int(co2b['Total'][len(co2b['Year']) - 1])) / int(
                    co2b['Total'][len(co2b['Year']) - 1])
            elif co2b['Year'][0] <= firsttime and co2b['Year'][len(co2b['Year']) - 1] < secondtime:
                shuzhi = (int(
                    co2b.loc[co2b['Year'] == firsttime]['Total'] - int(co2b['Total'][len(co2b['Year']) - 1])) / int(
                    co2b['Total'][len(co2b['Year']) - 1]))

            zuihouco2 = format(shuzhi, '.1%')
        #         co2_list.append([countryda, country, zuihou])
        except:
            zuihouco2 = None

        di_lst.append(
            dict(long=str(b['lng'][digui]), lat=str(b['lat'][digui]), popu=b['population'][digui], tempRate=zuihou,
                 co2Rate=zuihouco2))
        digui += 1
    return JsonResponse(di_lst, safe=False)
# Create your views here.
