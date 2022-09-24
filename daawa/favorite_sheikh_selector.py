from.models import(Favorite_sheikhs)


def get_favorite_sheikhs():
    return Favorite_sheikhs.objects.all()

def get_favorite_sheikh(favorite_sheikh_id):
    return Favorite_sheikhs.objects.get(pk=favorite_sheikh_id)