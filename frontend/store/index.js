export const actions = {
	async getPosts() {
		let res = await this.$axios.get("/blog/");
		return res;
	}
}