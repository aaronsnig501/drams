export default function ({ $axios }, inject) {
    const api = $axios.create({
        headers: {}
    })

    inject("api", api);
}
