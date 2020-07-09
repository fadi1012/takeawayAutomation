API_PROTOCOL = "https"
HOST = "gorest.co.in"
API_PREFIX = '%s://%s/public-api' % (API_PROTOCOL, HOST)
# User
USERS = API_PREFIX + '/users'
USER_BY_FIRST_NAME = USERS + '?first_name={}'
USER_BY_ID = USERS + '/{}'
# POSTS
POSTS = API_PREFIX + '/posts'
POST_BY_ID = POSTS + '/{}'
# PHOTO
PHOTOS = API_PREFIX + '/photos'
PHOTO_BY_ID = PHOTOS + '/{}'
# COMMENTS
COMMENTS = API_PREFIX + '/comments'
COMMENT_BY_ID = COMMENTS + '/{}'
# ALBUMS
ALBUMS = API_PREFIX + '/albums'
ALBUM_BY_ID = ALBUMS + '/{}'
