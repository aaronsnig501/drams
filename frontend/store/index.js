export const actions = {
  async getPosts() {
    let res = await this.$axios.get("/blog/");
    return res;
  },

  async getWhiskies(context, searchParams) {
    let { data } = await this.$axios.get("/api/whiskey/", {
      params: {
        search: searchParams
      }
    });
    return data;
  }
}