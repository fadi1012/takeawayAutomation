API_PROTOCOL = "http"
HOST = "gorest.co.in"
API_PREFIX = '%s://%s/public-api' % (API_PROTOCOL, HOST)
# User
USERS = API_PREFIX + '/users'
USER_BY_FIRST_NAME = USERS + '?first_name={}'
USER_BY_ID = USERS + '/{}'
# POSTS
POSTS = API_PREFIX + '/posts'
POST_BY_ID = POSTS + '/{}'
