from PIL import Image

def generate_profile_thumbnail(profile_id, filename, w, h):
    thumb = Image.open('media/' + filename)
    size = w, h
    thumb.thumbnail(size, Image.ANTIALIAS)
    thumb_filename = filename.split("/")[-1]
    thumb_file_path = 'profile_thumbs/{}'.format('thumb_' + str(profile_id) + '_' + thumb_filename)
    thumb.save('media/' + thumb_file_path)
    return thumb_file_path