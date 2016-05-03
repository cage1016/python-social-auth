"""
myQnapcloud OAuth2 backend docs at:
    http://wiki.myqnapcloud.com/mediawiki/index.php/QNAP_Account_Center_OAuth2_Introduction
"""

__author__ = 'cage.chung@gmail.com'

from six.moves.urllib.parse import urljoin
from social.backends.oauth import BaseOAuth2


class MyQnapCloudOAuth2(BaseOAuth2):
    """
    myQnapCloud OAuth authentication backend
    """

    ID_KEY = 'user_id'
    name = 'myqnapcloud'
    API_URL = 'https://dev-auth.dev-myqnapcloud.com/v1.1/'
    AUTHORIZATION_URL = 'https://dev-auth.dev-myqnapcloud.com/oauth/auth'
    ACCESS_TOKEN_URL = 'https://dev-auth.dev-myqnapcloud.com/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    EXTRA_DATA = [
        ('created_at', 'created_at')
    ]

    def api_url(self):
        return self.API_URL

    def get_user_details(self, response):
        """Return user details from myQnapcloud account"""
        fullname, first_name, last_name = self.get_user_names(
            None, response.get('first_name'), response.get('last_name')
        )
        return {'username': response.get('display_name'),
                'email': response.get('email') or '',
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name,
                'avatars': response.get('avatars')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        data = self._user_data(access_token)
        return data['result']

    def _user_data(self, access_token, path=None):
        url = urljoin(self.api_url(), 'me{0}'.format(path or ''))
        return self.get_json(url, params={'access_token': access_token})
