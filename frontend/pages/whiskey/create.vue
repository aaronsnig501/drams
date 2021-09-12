<template>
  <main>
    <navigation></navigation>

    <section class="section">
      <div class="columns heading-section">
        <div class="column is-1"></div>
        <div class="column is-11">
          <h1 class="is-size-2">Add new whiskey</h1>
        </div>
      </div>
      <div class="columns main-section">
        <div class="column is-2"></div>
        <div class="column is-8">

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Brand Name</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="select control is-fullwidth">
                  <select id="brand_name" v-model="whiskey.brandName">
                    <option value="1">Johnnie Walker</option>
                    <option value="2">Bushmills</option>
                    <option value="3">Jameson</option>
                    <option value="4">Jack Daniel's</option>
                    <option value="5">Roe & Co</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Name</label>
            </div>
            <div class="field-body">
              <div class="field">
                <p class="control">
                  <input class="input" id="name" type="text" v-model="whiskey.name" />
                </p>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Age Statement</label>
            </div>
            <div class="field-body">
              <div class="field">
                <p class="control">
                  <input class="input" id="age_statement" type="number" v-model="whiskey.ageStatement" />
                </p>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Proof</label>
            </div>
            <div class="field-body">
              <div class="field">
                <p class="control">
                  <input class="input" id="proof" type="number" v-model="whiskey.proof" />
                </p>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Colouring</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div id="colour" class="select control is-fullwidth">
                  <select v-model="whiskey.colour">
                    <option value="0">Unknown</option>
                    <option value="1">Artificial</option>
                    <option value="2">Natural</option>
                  </select>
                </div>
              </div>
            </div>
          </div>

         <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Chill filtering</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div id="chill_filtered" class="select control is-fullwidth">
                  <select v-model="whiskey.chillFiltered">
                    <option value="0">Unknown</option>
                    <option value="1">Chill filtered</option>
                    <option value="2">No chill filtering</option>
                  </select>
                </div>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Type</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div id="type" class="select control is-fullwidth">
                  <select v-model="whiskey.type">
                    <option value="1">Bourbon</option>
                    <option value="2">Rye</option>
                    <option value="3">Scotch</option>
                    <option value="4">Irish</option>
                    <option value="5">Japanese</option>
                  </select>
                </div>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Description</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control is-fullwidth">
                  <textarea id="description" class="textarea" placeholder="Whiskey Description" v-model="whiskey.description"></textarea>
                </div>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-label is-normal">
              <label class="label">Image</label>
            </div>
            <div class="field-body">
              <div class="field">
                <div class="control is-fullwidth">
                  <template>
                    <b-field id="image" class="file is-fullwidth" :class="{'has-name': !! whiskey.image}">
                      <b-upload v-model="whiskey.image" class="file-label">
                        <span class="file-cta">
                          <b-icon class="file-icon" icon="upload"></b-icon>
                          <span class="file-label">Click to upload</span>
                        </span>
                        <span class="file-name" v-if="whiskey.image">
                          {{ whiskey.image.name }}
                        </span>
                      </b-upload>
                    </b-field>
                  </template>
                </div>
              </div>
            </div>
          </div>

          <div class="buttons has-addons is-centered mt-6">
            <button class="button">Cancel</button>
            <button class="button is-primary" @click.prevent="createWhiskey">Create whiskey</button>
          </div>

        </div>
      </div>
    </section>
  </main>
</template>

<script>
  export default {
    data() {
      return {
        whiskey: {
          brandName: 1,
          name: "",
          ageStatement: 0,
          proof: 0,
          colour: 0,
          chillFiltered: 0,
          type: "",
          description: "",
          image: null
        }
      }
    },

    methods: {
      async createWhiskey() {
        const formData = new FormData();

        formData.append("brand", this.whiskey.brandName)
        formData.append("name", this.whiskey.name);
        formData.append("age_statement", this.whiskey.ageStatement);
        formData.append("proof", this.whiskey.proof);
        formData.append("colour", this.whiskey.colour);
        formData.append("chill_filtered", this.whiskey.chillFiltered);
        formData.append("type", this.whiskey.type);
        formData.append("description", this.whiskey.description);
        formData.append("image", this.whiskey.image);
        formData.append("added_by", this.$auth.user.id)

        try {
          let response = await this.$axios.post("/api/whiskey/", formData);
        } catch (error) {
          console.log(typeof error.response.data)
          for (const [field, message] of Object.entries(error.response.data)) {
            document.querySelector(`#${field}`).classList.add("is-danger");
          }
          this.$buefy.toast.open({
            indefinite: true,
            message: `Looks like your form has some errors.`,
            position: 'is-bottom-left',
            type: 'is-danger'
          })
        }
      }
    }
  }
</script>