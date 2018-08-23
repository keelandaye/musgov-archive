from django.shortcuts import render
from django.template.defaulttags import register
from django.db.models import Q

from bills.models import Bill, House

def index(request):
    pass


def houselist(request):
    house_list = House.objects.all()
    houses = {}

    for house in house_list:
        house_dict = {
            'house_name': house.house_name,
            'house_code': house.house_code,
            'logo_url': house.logo_url,
        }
        houses[str(house.id)] = house_dict

    template_name = 'api/houselist.html'
    context = {'houses': houses}

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    return render(request, template_name, context)


def is_pk(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def housedetail(request, ident):

    try:
        if is_pk(ident):
            house = House.objects.get(pk=ident)
        else:
            try:
                ident = ident.replace("_", " ")
                house = House.objects.get(house_name=ident)
            except House.DoesNotExist:
                try:
                    house = House.objects.get(house_code=ident.upper())
                except House.DoesNotExist:
                    template_name = 'api/fail.html'
                    return render(request, template_name)
    except House.DoesNotExist:
        template_name = 'api/fail.html'
        return render(request, template_name)

    houses = {}

    house_dict = {
        'house_name': house.house_name,
        'house_code': house.house_code,
        'logo_url': house.logo_url,
    }
    houses[str(house.id)] = house_dict

    template_name = 'api/housedetail.html'
    context = {'houses': houses}

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    return render(request, template_name, context)


def billlist(request):
    bill_list = Bill.objects.all()
    bills = {}

    for bill in bill_list:
        bill_dict = {
            'bill_number': bill.bill_number,
            'bill_name': bill.bill_name,
            'bill_house': bill.bill_house.id,
            'bill_content': bill.bill_content,
            'date_first_posted': bill.date_first_posted,
        }
        bills[str(bill.id)] = bill_dict

    template_name = 'api/billlist.html'
    context = {'bills': bills}

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    return render(request, template_name, context)


def billdetail(request, house="", number="", name=""):

    if house != "" and number != "":
        try:
            if is_pk(house):
                house = House.objects.get(pk=house)
            else:
                try:
                    house = house.replace("_", " ")
                    house = House.objects.get(house_name=house)
                except House.DoesNotExist:
                    try:
                        house = House.objects.get(house_code=house.upper())
                    except House.DoesNotExist:
                        template_name = 'api/fail.html'
                        return render(request, template_name)
        except House.DoesNotExist:
            template_name = 'api/fail.html'
            return render(request, template_name)
        try:
            bill = Bill.objects.get(Q(bill_house=house) & Q(bill_number=number))
        except Bill.DoesNotExist:
            template_name = 'api/fail.html'
            return render(request, template_name)
    elif name != "":
        name = name.replace("_", " ")
        bill = Bill.objects.get(bill_name=name)
    else:
        template_name = 'api/fail.html'
        return render(request, template_name)

    bills = {}

    bill_dict = {
        'bill_number': bill.bill_number,
        'bill_name': bill.bill_name,
        'bill_house': bill.bill_house.id,
        'bill_content': bill.bill_content,
        'date_first_posted': bill.date_first_posted,
    }
    bills[str(bill.id)] = bill_dict

    template_name = 'api/billdetail.html'
    context = {'bills': bills}

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    return render(request, template_name, context)


def housebills(request, ident):

    try:
        if is_pk(ident):
            house_obj = House.objects.get(pk=ident)
            bill_list = Bill.objects.filter(bill_house=house_obj)
        else:
            try:
                ident = ident.replace("_", " ")
                house_obj = House.objects.get(house_name=ident)
                bill_list = Bill.objects.filter(bill_house=house_obj)
            except House.DoesNotExist:
                try:
                    house_obj = House.objects.get(house_code=ident.upper())
                    bill_list = Bill.objects.filter(bill_house=house_obj)
                except House.DoesNotExist:
                    template_name = 'api/fail.html'
                    return render(request, template_name)
    except House.DoesNotExist:
        template_name = 'api/fail.html'
        return render(request, template_name)

    bills = {}

    for bill in bill_list:
        bill_dict = {
            'bill_number': bill.bill_number,
            'bill_name': bill.bill_name,
            'bill_house': bill.bill_house.id,
            'bill_content': bill.bill_content,
            'date_first_posted': bill.date_first_posted,
        }
        bills[str(bill.id)] = bill_dict

    template_name = 'api/billlist.html'
    context = {'bills': bills}

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    return render(request, template_name, context)
