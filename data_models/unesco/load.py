import csv  # https://docs.python.org/3/library/csv.html

from unesco.models import Category, States, Region, ISO, Site

fhand = open('unesco/whc-sites-2018-small.csv')
reader = csv.reader(fhand)

Category.objects.all().delete()
States.objects.all().delete()
Region.objects.all().delete()
ISO.objects.all().delete()
Site.objects.all().delete()

# Format
# jane@tsugi.org,I,Python
# ed@tsugi.org,L,Python

for row in reader:

    try:
        c = Category.objects.get(name=row[7])
    except:
        print("Inserting category",row[7])
        c = Category(name=row[7])
        c.save()

    try:
        s = States.objects.get(name=row[8])
    except:
        print("Inserting state",row[8])
        s = States(name=row[8])
        s.save()

    try:
        r = Region.objects.get(name=row[9])
    except:
        print("Inserting region",row[9])
        r = Region(name=row[9])
        r.save()

    try:
        i = ISO.objects.get(name=row[10])
    except:
        print("Inserting iso",row[10])
        i = ISO(name=row[10])
        i.save()


    try:
        y = int(row[3])
    except:
        y = None

    try:
        lon = float(row[4])
    except:
        lon = None

    try:
        lat = float(row[5])
    except:
        lat = None

    try:
        a = float(row[6])
    except:
        a = None

    f = Site(name = row[0], category=c, states=s, region=r, ISO=i, description=row[1], justification=row[2], year=y, longitude=lon, latitude=lat, area_hectares=a)
    f.save()

