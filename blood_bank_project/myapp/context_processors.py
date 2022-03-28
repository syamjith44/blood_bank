from .models import District, Center


def menu_objects(request):
    district_objects = District.objects.all()
    center_objects = Center.objects.all()

    return dict(district_objects=district_objects, center_objects=center_objects)