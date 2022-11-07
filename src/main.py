import requests
from uuid import uuid4

class MAIN:
	def __init__(self, device_id: str = None):
		self.api = "https://app.main.community"
		self.device_id = self.generate_device_id() if not device_id else device_id
		self.headers = {
			"locale": "en_US",
			"deviceid": self.device_id,
			"user-agent": "android/3.15.0"
		}
		self.user_id = None
		self.access_token = None


	def generate_device_id(self):
		return str(uuid4())

	def register(
			self,
			country_id: int,
			nickname: str,
			social_network_id: int,
			social_network_token: str,
			invite_code: str = None):
		data = {
			"countryId": country_id,
			"nickname": nickname,
			"socialNetwork": social_network_id,
			"socialNetworkToken": social_network_token
		}
		if invite_code:
			data["invite"] = invite_code
		return requests.post(
			f"{self.api}/auth/registerv2",
			json=data,
			headers=self.headers).json()

	def login_with_google(self, google_id_token: str):
		data = {
			"socialNetwork": 3,
			"socialNetworkToken": google_id_token
		}
		response = requests.post(
			f"{self.api}/auth/login",
			json=data,
			headers=self.headers).json()
		if "id" in response:
			self.user_id = response["id"]
			self.access_token = response["token"]
			self.headers["access-token"] = self.access_token
		return response

	def login_with_access_token(self, access_token: str):
		self.access_token = access_token
		self.headers["access-token"] = self.access_token
		response = self.get_account_info()
		self.user_id = response["id"]
		return response

	def get_account_info(self):
		return requests.get(
			f"{self.api}/users/me",
			headers=self.headers).json()

	def get_account_profile(self):
		return requests.get(
			f"{self.api}/users/me/profile",
			headers=self.headers).json()

	def get_account_activity(self):
		return requests.get(
			f"{self.api}/users/me/activity",
			headers=self.headers).json()

	def get_account_wallet(self):
		return requests.get(
			f"{self.api}/users/me/wallet",
			headers=self.headers).json()

	def get_auth_web_token(self):
		return requests.get(
			f"{self.api}/auth/getWebToken",
			headers=self.headers).json()

	def get_prices_info(self):
		return requests.get(
			f"{self.api}/info/prices",
			headers=self.headers).json()

	def get_unread_notifications(self):
		return requests.get(
			f"{self.api}/notifications/unread",
			headers=self.headers).json()

	def get_boardclaims_notifications(self):
		return requests.get(
			f"{self.api}/notifications/boardclaims",
			headers=self.headers).json()

	def get_feed(
			self,
			limit: int = 40,
			offset: int = 0,
			type: int = None,
			region: int = None,
			categories: int = None,
			sort_period: str = None):
		url = f"{self.api}/feed?limit={limit}&offset={offset}"
		if type:
			url += f"&type={type}"
		if region:
			url += f"&region={region}"
		if categories:
			url += f"&categories={categories}"
		if sort_period:
			url += f"&sortPeriod={sort_period}"
		return requests.get(
			url, headers=self.headers).json()

	def get_topics(self):
		return requests.get(
			f"{self.api}/tags/topics",
			headers=self.headers).json()

	def get_rocket_price(self):
		return requests.get(
			f"{self.api}/info/rocketprice",
			headers=self.headers).json()

	def subscribe_tag(self, tag_id: int):
		return requests.put(
			f"{self.api}/tags/{tag_id}/subscribe",
			headers=self.headers).status_code

	def unsubscribe_tag(self, tag_id: int):
		return requests.put(
			f"{self.api}/tags/{tag_id}/unsubscribe",
			headers=self.headers).status_code

	def get_user_info(self, user_id: int):
		return requests.get(
			f"{self.api}/users/{user_id}",
			headers=self.headers).json()

	def get_user_wallet(self, user_id: int):
		return requests.get(
			f"{self.api}/users/{user_id}/wallet",
			headers=self.headers).json()		

	def get_user_followings(
			self,
			user_id: int,
			limit: int = 40,
			offset: int = 0):
		return requests.get(
			f"{self.api}/users/{user_id}/followed?limit={limit}&offset={offset}",
			headers=self.headers).json()

	def get_user_followers(
			self,
			user_id: int,
			limit: int = 40,
			offset: int = 0):
		return requests.get(
			f"{self.api}/users/{user_id}/followers?limit={limit}&offset={offset}",
			headers=self.headers).json()

	def get_user_posts(
			self,
			user_id: int,
			limit: int = 40,
			offset: int = 0,
			type: int = None):
		url = f"{self.api}/users/{user_id}/posts?limit={limit}&offset={offset}"
		if type:
			url += f"&type={type}"
		return requests.get(
			url, headers=self.headers).json()

	def get_user_comments(
			self,
			user_id: int,
			limit: int = 20,
			offset: int = 0):
		return requests.get(
			f"{self.api}/users/{user_id}/comments?offset={offset}&limit={limit}",
			headers=self.headers).json()

	def get_user_owned_tags(
			self,
			user_id: int,
			limit: int = 100,
			offset: int = 0):
		return requests.get(
			f"{self.api}/users/{user_id}/ownedTags?offset={offset}&limit={limit}",
			headers=self.headers).json()

	def get_user_moderated_tags(
			self,
			user_id: int,
			limit: int = 100,
			offset: int = 0):
		return requests.get(
			f"{self.api}/users/{user_id}/moderatedTags?offset={offset}&limit={limit}",
			headers=self.headers).json()

	def get_referral(self):
		return requests.get(
			f"{self.api}/referral",
			headers=self.headers).json()

	def get_post_info(self, post_id: int):
		return requests.get(
			f"{self.api}/posts/{post_id}",
			headers=self.headers).json()

	def get_post_comments(
			self,
			post_id: int,
			offset: int = 0,
			limit: int = 40,
			nested: int = None):
		url = f"{self.api}/posts/{post_id}/comments?offset={offset}&limit={limit}"
		if nested:
			url += f"&nested={nested}"
		return requests.get(
			url, headers=self.headers).json()

	def like_post(self, post_id: int):
		return requests.put(
			f"{self.api}/posts/{post_id}/like",
			headers=self.headers).json()

	def dislike_post(self, post_id: int):
		return requests.put(
			f"{self.api}/posts/{post_id}/dislike",
			headers=self.headers).json()

	def norate_post(self, post_id: int):
		return requests.post(
			f"{self.api}/posts/{post_id}/norate",
			headers=self.headers).json()

	def share_post(self, post_id: int):
		return requests.put(
			f"{self.api}/posts/{post_id}/share",
			headers=self.headers).json()

	def vote_post(self, post_id: int):
		return requests.put(
			f"{self.api}/posts/{post_id}/vote",
			headers=self.headers).json()

	def comment_post(
			self,
			post_id: int,
			content: str,
			code: str = None,
			height: int = 1,
			id: int = 0,
			label: str = None,
			preview_url: str = None,
			source_url: str = None,
			text: str = None,
			type: int = -1,
			width: int = 1,
			reply_comment_id: int = 0):
		data = {
			"mediaItem": {},
			"replyCommentId": reply_comment_id,
			"text": content
		}
		if code:
			data["mediaItem"]["code"] = cpde
		if height:
			data["mediaItem"]["height"] = height,
		if id:
			data["mediaItem"]["id"] = id
		if label:
			data["mediaItem"]["label"] = label
		if preview_url:
			data["mediaItem"]["previewUrl"] = preview_url
		if source_url:
			data["mediaItem"]["sourceUrl"] = source_url
		if text:
			data["mediaItem"]["text"] = text
		if type:
			data["mediaItem"]["type"] = type
		if width:
			data["mediaItem"]["width"] = width
		return requests.post(
			f"{self.api}/comments/{post_id}",
			json=data,
			headers=self.headers).json()

	def edit_comment(
			self,
			comment_id: int,
			text: str):
		data = {
			"text": text
		}
		return requests.put(
			f"{self.api}/comments/{comment_id}",
			json=data,
			headers=self.headers).json()

	def delete_comment(self, comment_id: int):
		return requests.delete(
			f"{self.api}/comments/{comment_id}",
			headers=self.headers).json()

	def like_comment(self, comment_id: int):
		return requests.put(
			f"{self.api}/comments/{comment_id}/like",
			headers=self.headers).json()

	def dislike_comment(self, comment_id: int):
		return requests.put(
			f"{self.api}/comments/{comment_id}/dislike",
			headers=self.headers).json()

	def norate_comment(self, comment_id: int):
		return requests.post(
			f"{self.api}/comments/{comment_id}/norate",
			headers=self.headers).json()

	def edit_profile(
			self,
			description: str = None,
			avatar_preview_url: str = None):
		data = {}
		if description:
			data["description"] = description
		if avatar_preview_url:
			data["avatarPreviewUrl"] = avatar_preview_url
		return requests.put(
			f"{self.api}/users/me",
			json=data,
			headers=self.headers).json()

	def explore(
			self,
			limit: int = 40,
			offset: int = 0,
			coins: int = 1,
			favorites: int = 1,
			promoted: int = 1):
		url = f"{self.api}/explore?limit={limit}&offset={offset}"
		if coins:
			url += f"&coins={coins}"
		if favorites:
			url += f"&favorites={favorites}"
		if promoted:
			url += f"&promoted={promoted}"
		return requests.get(
			url, headers=self.headers).json()

	def get_tag_info(self, tag_id: int):
		return requests.get(
			f"{self.api}/tags/{tag_id}",
			headers=self.headers).json()

	def get_tag_activity(self, tag_id: int):
		return requests.get(
			f"{self.api}/tags/{tag_id}/activity",
			headers=self.headers).json()

	def get_tag_moderators(self, tag_id: int):
		return requests.get(
			f"{self.api}/tags/{tag_id}/moderators",
			headers=self.headers).json()

	def get_tag_rules(self, tag_id: int):
		return requests.get(
			f"{self.api}/tags/{tag_id}/rules",
			headers=self.headers).json()

	def get_tag_activity_rating(
			self,
			tag_id: int,
			limit: int = 40,
			offset: int = 0):
		return requests.get(
			f"{self.api}/tags/{tag_id}/activity_rating?limit={limit}&offset={offset}",
			headers=self.headers).json()

	def search_users(
			self,
			query: str,
			limit: int = 40,
			offset: int = 0):
		return requests.get(
			f"{self.api}/users?search={query}&limit={limit}&offset={offset}",
			headers=self.headers).json()

	def search_tags(
			self,
			query: str,
			limit: int = 40,
			offset: int = 0,
			foreign: int = 1):
		return requests.get(
			f"{self.api}/users?search={query}&limit={limit}&offset={offset}&foreign={foreign}",
			headers=self.headers).json()

	def get_notifications(
			self,
			limit: int = 40,
			offset: int = 0):
		return requests.get(
			f"{self.api}/notifications?offset={offset}&limit={limit}",
			headers=self.headers).json()

	def delete_post(self, post_id: int):
		return requests.delete(
			f"{self.api}/posts/{post_id}",
			headers=self.headers).status_code

	def block_user(self, user_id: int):
		return requests.put(
			f"{self.api}/users/{user_id}/blacklist/add",
			headers=self.headers).status_code

	def unblock_user(self, user_id: int):
		return requests.put(
			f"{self.api}/users/{user_id}/blacklist/remove",
			headers=self.headers).status_code

	def mute_user(self, user_id: int):
		return requests.put(
			f"{self.api}/users/{user_id}/mute",
			headers=self.headers).status_code

	def unmute_user(self, user_id: int):
		return requests.put(
			f"{self.api}/users/{user_id}/unmute",
			headers=self.headers).status_code

	def report_user(
			self,
			user_id: int,
			report_type: int):
		data = {
			"claimType": report_type
		}
		return requests.post(
			f"{self.api}/users/{user_id}/claim",
			json=data,
			headers=self.headers).status_code
