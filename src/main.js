class Main {
	constructor(language = "en") {
		this.api = "https://app.main.community"
		this.deviceId = this.generateDeviceId()
		this.headers = {
			"locale": "en_US",
			"deviceid": this.deviceId,
			"user-agent": "android/3.15.0"
		}
	}

	generateDeviceId() {
		return uuid4().toString()
	}

	async register(
			countryId,
			nickname,
			socialNetworkId,
			socialNetworkToken,
			inviteCode = null) {
		let body = {
			countryId: coutnryId,
			nickname: nickname,
			socialNetwork: socialNetworkId,
			socialNetworkToken: socialNetworkToken
		}
		if (inviteCode) {
			body.invite = inviteCode
		}
		const response = await fetch(
			`${this.api}/auth/registerv2`, {
				method: "POST",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.json()
	}

	async loginWithGoogle(googleIdToken) {
		const response = await fetch(
			`${this.api}/auth/login`, {
				method: "POST",
				body: JSON.stringify({
					socialNetwork: 3,
					socialNetworkToken: googleIdToken
				}),
				headers: this.headers
			})
		data = await response.json()
		if ("id" in data) {
			this.userId = data.id
			this.accessToken = data.token
			this.headers["access-token"] = this.accessToken
		}
		return data
	}

	async getAccountInfo() {
		const response = await fetch(
			`${this.api}/users/me`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAccountProfile() {
		const response = await fetch(
			`${this.api}/users/me/profile`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAccountActivity() {
		const response = await fetch(
			`${this.api}/users/me/activity`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAccountWallet() {
		const response = await fetch(
			`${this.api}/users/me/wallet`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAuthWebToken() {
		const response = await fetch(
			`${this.api}/auth/getWebToken`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPricesInfo() {
		const response = await fetch(
			`${this.api}/info/prices`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUnreadNotifications() {
		const response = await fetch(
			`${this.api}/notifications/unread`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getBoardClaimsNotifications() {
		const response = await fetch(
			`${this.api}/notifications/boardclaims`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getFeed(
			limit = 40,
			offset = 0,
			type = null,
			region = null,
			categories = null,
			sortPeriod = null) {
		let url = `${this.api}/feed?limit=${limit}&offset=${offset}`
		if (type) {
			url += `&type=${type}`
		}
		if (region) {
			url += `&region=${region}`
		}
		if (categories) {
			url += `&categories=${categories}`
		}
		if (sortPeriod) {
			url += `&sortPeriod=${sortPeriod}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getTopics() {
		const response = await fetch(
			`${this.api}/tags/topics`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getRocketPrice() {
		const response = await fetch(
			`${this.api}/info/rocketprice`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserInfo(userId) {
		const response = await fetch(
			`${this.api}/users/${userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserWallet(userId) {
		const response = await fetch(
			`${this.api}/users/${userId}/wallet`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserFollowers(userId, limit = 40, offset = 0) {
		const response = await fetch(
			`${this.api}/users/${userId}/followers?limit=${limit}&offset=${offset}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserFollowings(userId, limit = 40, offset = 0) {
		const response = await fetch(
			`${this.api}/users/${userId}/followed?limit=${limit}&offset=${offset}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserPosts(userId, limit = 40, offset = 0, type = null) {
		let url = `${this.api}/users/${userId}/posts?limit=${limit}&offset=${offset}`
		if (type) {
			url += `&type=${type}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserComments(limit = 20, offset = 0) {
		const response = await fetch(
			`${this.api}/users/${userId}/comments?limit=${limit}&offset=${offset}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserOwnedTags(limit = 20, offset = 0) {
		const response = await fetch(
			`${this.api}/users/${userId}/ownedTags?limit=${limit}&offset=${offset}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserModeratedTags(limit = 20, offset = 0) {
		const response = await fetch(
			`${this.api}/users/${userId}/moderatedTags?limit=${limit}&offset=${offset}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getReferral() {
		const response = await fetch(
			`${this.api}/referral`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPostInfo(postId) {
		const response = await fetch(
			`${this.api}/posts/${postId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPostComments(postId, limit = 40, offset = 0, nested = null) {
		let url = `${this.api}/posts/${postId}/comments?limit=${limit}&offset=${offset}`
		if (nested) {
			url += `&nested=${nested}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async likePost(postId) {
		const response = await fetch(
			`${this.api}/posts/${postId}/like`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async dislikePost(postId) {
		const response = await fetch(
			`${this.api}/posts/${postId}/dislike`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async noRatePost(postId) {
		const response = await fetch(
			`${this.api}/posts/${postId}/norate`, {
				method: "POST",
				headers: this.headers
			})
		return response.json()
	}

	async sharePost(postId) {
		const response = await fetch(
			`${this.api}/posts/${postId}/share`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async votePost(postId) {
		const response = await fetch(
			`${this.api}/posts/${postId}/vote`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async editProfile(description = null, avatarPreviewUrl = null) {
		let body  = {}
		if (description) {
			body.description = description
		}
		if (avatarPreviewUrl) {
			body.avatarPreviewUrl = avatarPreviewUrl
		}
		const response = await fetch(
			`${this.api}/users/me`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async getNotifications(limit = 20, offset = 0) {
		const response = await fetch(
			`${this.api}/notifications?limit=${limit}&offset=${offset}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async blockUser(userId) {
		const response = await fetch(
			`${this.api}/users/${userId}/blacklist/add`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async unblockUser(userId) {
		const response = await fetch(
			`${this.api}/users/${userId}/blacklist/remove`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async blockUser(userId) {
		const response = await fetch(
			`${this.api}/users/${userId}/mute`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}

	async unblockUser(userId) {
		const response = await fetch(
			`${this.api}/users/${userId}/unmute`, {
				method: "PUT",
				headers: this.headers
			})
		return response.json()
	}
}

module.exports = {Main}
