import json
from social.tests.backends.oauth import OAuth2Test


class MyQnapCloudOAuth2Test(OAuth2Test):
    backend_path = 'social.backends.myqnapcloud.MyQnapCloudOAuth2'
    user_data_url = 'https://account.alpha-myqnapcloud.com/v1.1/me'
    expected_username = 'Cage'
    access_token_body = json.dumps({
        'access_token': 'foobar',
        'token_type': 'bearer'
    })

    user_data_body = json.dmps({
        'last_name': 'CHUNG',
        'pdated_at': '2015-09-23T09:38:50.054000',
        'token_type': 'Bearer',
        'birthday': '1982-10-16',
        'mobile_nmber': '-',
        'ser_id': '560272b648cfd023501c987',
        'email_delivery_date': None,
        'first_name': 'KAI CHU',
        'sbscribed': True,
        'display_name': 'Cage',
        'email_delivery_stats': '',
        'langage': 'en',
        'access_token': '2.nqyxWN5ljpXTtLfpZmb7Ge2EAfmYJS6SkqGaKM.144661068',
        'gender': 1,
        'created_at': '2015-09-23T09:36:54.934000',
        'expires_in': 76263,
        'portal_notify': True,
        'simple_token': 'd966d03e8a0b68137ae929a40eaac73d',
        'scope': ['ser'],
        'email': 'cage.chng@live.com'
    })

    def test_login(self):
        self.do_login()
