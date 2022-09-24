from.models import(Islam_serie_episode)


def get_islam_episodes_lectures():
    return Islam_serie_episode.objects.all()

def get_islam_episode_lecture(episode_lecture_id):
    return Islam_serie_episode.objects.get(pk=episode_lecture_id)