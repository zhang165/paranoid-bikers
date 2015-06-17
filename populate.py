import os

def populate():

    add_placemark(
        id='123',
        name="Official Django Tutorial",
        description="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        lat = 123,
        lon = 4321,)

    add_placemark(
        id='123asdjfaklsjfa;skdjf;aslkdfja',
        name="Official Django Tutorial12312312312312",
        description="https://docs.djajas;ldfjo9jralskdfj;aslkdfngoproject.com/en/1.5/intro/tutorial01/",
        lat = 123.123,
        lon = 4321.432,)

    add_placemark(
        id='hello world',
        name="a name",
        description="description herealsdjf;alsk",
        lat = 123,
        lon = 4321,)


def add_placemark(id, name, description, lat=1, lon=2):
    p = Placemark.objects.get_or_create(placemark_id = id, name = name, description = description, lat = lat, lon = lon)[0]
    return p



# Start execution here!
if __name__ == '__main__':
    print ("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikers.settings')
    from parkingApp.models import Placemark
    populate()