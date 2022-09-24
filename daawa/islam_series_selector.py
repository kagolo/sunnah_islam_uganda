from.models import(Islam_series)


def get_islam_series_lectures():
    return Islam_series.objects.all()

def get_islam_serie_lecture(serie_lecture_id):
    return Islam_series.objects.get(pk=serie_lecture_id)