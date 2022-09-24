from.models import(All_sheikhs)


def get_all_sheikhs():
    return All_sheikhs.objects.all()

def get_lecture(lecture_id):
    return All_sheikhs.objects.get(pk=lecture_id)    